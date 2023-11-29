import redis from 'redis';

const client = redis.createClient({
  port: 6379,
  host: 'localhost',
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Create and Display Hash
const hashKey = 'HolbertonSchools';

const hashData = {
  'Portland': 50,
  'Seattle': 80,
  'New York': 20,
  'Bogota': 20,
  'Cali': 40,
  'Paris': 2,
};

Object.entries(hashData).forEach(([field, value]) => {
  client.hset(hashKey, field, value, redis.print);
});

client.hgetall(hashKey, (err, value) => {
  console.log(value);
});

