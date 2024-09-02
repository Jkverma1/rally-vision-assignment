        document.getElementById('uploadForm').addEventListener('submit', async (event) => {
            event.preventDefault();

            const fileInput = document.getElementById('imageUpload');
            const file = fileInput.files[0];

            if (!file) {
                alert('Please select an image file.');
                return;
            }

            const formData = new FormData();
            formData.append('file', file);
            const uploadResponse = await fetch('/detect-person', {
                method: 'POST',
                body: formData
            });

            if (!uploadResponse.ok) {
                document.getElementById('result').innerText = 'Error uploading image';
                return;
            }

            const uploadData = await uploadResponse.json();
            const taskId = uploadData.task_id;

            const checkResult = async () => {
                const resultResponse = await fetch(`/result/${taskId}`);
                if (resultResponse.ok) {
                    const resultData = await resultResponse.json();
                    document.getElementById('result').innerText = `Result: ${JSON.stringify(resultData)}`;
                } else {
                    setTimeout(checkResult, 2000); 
                }
            };

            checkResult();
        });