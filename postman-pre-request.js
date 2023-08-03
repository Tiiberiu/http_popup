// Make an API call and save JSON response data as environment variables
pm.sendRequest({
    url: 'http://localhost:5722/inputs?Param1=x&Param2=x&Param3=x', 
    method: 'GET',
    header: {
        // Add any required headers here
    },
}, function (err, response) {
    if (err) {
        console.error(err);
    } else {
        try {
            const jsonData = response.json(); // Assuming the response is in JSON format
            pm.environment.set('postman_param1', jsonData.Param1);
            pm.environment.set('postman_param2', jsonData.Param2);
            pm.environment.set('postman_param3', jsonData.Param3);
        } catch (e) {
            console.error('Error parsing JSON:', e);
        }
    }
});
