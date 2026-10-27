// geospatial-commands.js
// Run: mongosh --file geospatial-commands.js
// Purpose: store locations, index them and find the nearest ones.

db = db.getSiblingDB("shopdb");
db.stores.drop();

// 1. Store locations as GeoJSON points: [longitude, latitude]  (longitude FIRST)
db.stores.insertMany([
  { name: "North Nazimabad Store", location: { type: "Point", coordinates: [67.0330, 24.9420] } },
  { name: "Gulshan Store",         location: { type: "Point", coordinates: [67.0920, 24.9180] } },
  { name: "Saddar Store",          location: { type: "Point", coordinates: [67.0290, 24.8560] } },
  { name: "Clifton Store",         location: { type: "Point", coordinates: [67.0300, 24.8130] } }
]);

// 2. A 2dsphere index is required for distance searches
db.stores.createIndex({ location: "2dsphere" });

// 3. $near: stores within 8 km of a point, nearest first
const me = { type: "Point", coordinates: [67.0300, 24.9300] };
print("--- within 8 km ---");
printjson(db.stores.find(
  { location: { $near: { $geometry: me, $maxDistance: 8000 } } },   // metres
  { _id: 0, name: 1 }
).toArray());

// 4. $geoNear (aggregation stage): also returns the distance
print("--- distance to every store ---");
printjson(db.stores.aggregate([
  { $geoNear: { near: me, distanceField: "metres", spherical: true } },
  { $project: { _id: 0, name: 1, km: { $round: [{ $divide: ["$metres", 1000] }, 1] } } }
]).toArray());
