import redis from 'redis';
import { promisify } from 'util';

// Create Redis client
const client = redis.createClient();

// Promisify the client.get method for async/await
const getAsync = promisify(client.get).bind(client);

// Handle Redis connection events
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

// Function to set a new key-value pair in Redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Async function to retrieve and display a value for a given key
async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error(`Error fetching value for ${schoolName}: ${err.message}`);
  }
}

// Main function to run the tasks
(async function main() {
  await displaySchoolValue('Holberton');            // Display value for 'Holberton'
  setNewSchool('HolbertonSanFrancisco', '100');     // Set value for 'HolbertonSanFrancisco'
  await displaySchoolValue('HolbertonSanFrancisco'); // Display value for 'HolbertonSanFrancisco'
})();
