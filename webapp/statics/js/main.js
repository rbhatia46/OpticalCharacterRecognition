(function() {

    const form = document.getElementById('ocr-form');
    const fileType = document.getElementById('file-type');
    const inputFile = document.getElementById('input-file');
    const results = document.getElementById('results');

    form.onsubmit = (e) => {
        console.log('Sending data');
        e.preventDefault();

        const body = new FormData()
        body.append(fileType.value, inputFile.files[0]);
        console.log(body)
        sendDataToServer(body, fileType.value);
    }

    const sendDataToServer = async (body, file_type) => {
        try {
            const url = `http://localhost:5000/predict/${file_type}`;
            const options = getRequestOptions(body);
            console.log(url, options)

            const data = await (await fetch(url, options)).json();
            if (data.error) { throw new Error(data.error); }

            results.innerText = data.predicted_text;
        } catch(e) {
            console.error(e);
            results.innerText = `ERROR: ${e.message}`;
        }
    }

    const getRequestOptions = (body) => {
        const options = {
            headers: {
              'Accept': 'application/json',
            },
            method: "POST",
            body: body,
        }
        return options;
    }

})();
