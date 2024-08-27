import redis from 'redis';

// Create Redis client
const client = redis.createClient();

// Event handlers for connection and error
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

// Function to set a new key-value pair in Redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);  // Using redis.print to log status
}

// Function to retrieve and display a value for a given key
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, value) => {
    if (err) {
      console.error(err); // Handle errors properly
    } else {
      console.log(value); // Display the retrieved value
    }
  });
}

// Test the functions
displaySchoolValue('Holberton');  // Fetch value for 'Holberton' key
setNewSchool('HolbertonSanFrancisco', '100');  // Set value for 'HolbertonSanFrancisco'
displaySchoolValue('HolbertonSanFrancisco');  // Fetch value for 'HolbertonSanFrancisco' key
