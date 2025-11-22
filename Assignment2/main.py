import pandas as pd
import math

# Each analysis is preceeded by a print statement explaining what it is

csv_file = "Assignment2\\Data\\Hospitals.csv"
df = pd.read_csv(csv_file)

print(" Dataset Preview ")
print(df.head())

facilities_per_state = df.groupby("STATE").size()
print("\n Number of Facilities per STATE ")
print(facilities_per_state)

df_filtered = df[df["BEDS"] >= 0]

avg_beds_per_owner = df_filtered.groupby("OWNER")["BEDS"].mean().astype(int)
print("\n Average Beds per OWNER (BEDS >= 0) ")
print(avg_beds_per_owner)

trauma_centers = df[df["TRAUMA"].notna() & (df["TRAUMA"].str.upper() != "NOT AVAILABLE")]
print("\n Facilities with TRAUMA Centers ")
print(trauma_centers[["NAME", "CITY", "STATE", "TRAUMA"]])

top_cities = df.groupby("CITY").size().sort_values(ascending=False).head(5)
print("\n Top 5 Cities by Number of Facilities ")
print(top_cities)

state = "CA"
beds_threshold = 1000
filtered_hospitals = list(
    map(
        lambda row: row["NAME"],
        filter(
            lambda row: row["STATE"] == state and row["BEDS"] > beds_threshold,
            df.to_dict(orient="records")
        )
    )
)
print(f"\n Hospitals in {state} with more than {beds_threshold} beds ")
print(filtered_hospitals)

# Note: I did not do this math, the function was copied from an online source
def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    d_phi = math.radians(lat2 - lat1)
    d_lambda = math.radians(lon2 - lon1)
    a = math.sin(d_phi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(d_lambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c
##############################################################################

def nearest_n_hospitals(df, lat, lon, n=5):
    df["DISTANCE_KM"] = df.apply(lambda row: haversine(lat, lon, row["LATITUDE"], row["LONGITUDE"]), axis=1)
    nearest = df.sort_values("DISTANCE_KM").head(n)
    return nearest[["NAME", "ADDRESS", "CITY", "STATE", "DISTANCE_KM"]]

user_lat = 37.3387
user_lon = -121.8853
nearest = nearest_n_hospitals(df, user_lat, user_lon)
print(f"\n Top 5 Nearest Hospitals to {user_lat}, {user_lon}")
print(nearest)
