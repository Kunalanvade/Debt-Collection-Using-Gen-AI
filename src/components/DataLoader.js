import React, { useState } from 'react';

function DataLoader() {
    const [data, setData] = useState(null);
    const [error, setError] = useState(null);

    const handleLoadData = () => {
        fetch('http://localhost:8000/api/some-endpoint/')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                setData(data);
                console.log('Data:', data);
            })
            .catch(error => {
                setError(error.message);
                console.error('Error:', error);
            });
    };

    return (
        <div>
            <button onClick={handleLoadData}>Load Data</button>
            {error && <p>Error: {error}</p>}
            {data && (
                <div>
                    <h2>Data Loaded:</h2>
                    <pre>{JSON.stringify(data, null, 2)}</pre>
                </div>
            )}
        </div>
    );
}

export default DataLoader;
