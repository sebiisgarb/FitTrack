import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/api/users/2/`);
        setUser(response.data); // Axios automatically parses JSON
      } catch (err) {
        setError(err.message);
      }
    };
    fetchUser();
  }, []);

  return (
    <div className="App">
      <h1>{user ? user.username : "Loading..."}</h1>
    </div>
  );
}

export default App;
