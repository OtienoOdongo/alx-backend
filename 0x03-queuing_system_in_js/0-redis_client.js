// Importing the 'redis' library using the 'import' keyword
import redis from 'redis';

// Creating a Redis client with connection details
const client = redis.createClient({
  port: 6379,    // Redis server port
  host: 'localhost',  // Redis server host
});

// Event handler for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event handler for connection errors
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});
