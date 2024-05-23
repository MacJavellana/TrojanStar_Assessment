
    document.querySelectorAll('.edit-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const recipeId = btn.dataset.id;
            fetch(`/recipes/${recipeId}`)
                .then(response => response.json())
                .then(data => {
                    document.getElementById('edit-recipe-id').value = data.id;
                    document.getElementById('edit-recipe-name').value = data.name;
                    document.getElementById('edit-recipe-ingredients').value = data.ingredients;
                    document.getElementById('edit-recipe-steps').value = data.steps;
                    document.getElementById('edit-recipe-preparation-time').value = data.preparation_time;
                    document.getElementById('edit-modal').style.display = 'block';
                })
                .catch(error => console.error('Error:', error));
        });
    });

    document.getElementById('edit-form').addEventListener('submit', event => {
        event.preventDefault();
        const recipeId = document.getElementById('edit-recipe-id').value;
        const formData = {
            name: document.getElementById('edit-recipe-name').value,
            ingredients: document.getElementById('edit-recipe-ingredients').value,
            steps: document.getElementById('edit-recipe-steps').value,
            preparation_time: document.getElementById('edit-recipe-preparation-time').value
        };
        fetch(`/recipes/${recipeId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        })
        .then(response => {
            if (response.ok) {
                window.location.reload();
            } else {
                throw new Error('Failed to update recipe');
            }
        })
        .catch(error => console.error('Error:', error));
    });

    const form = document.getElementById('searchForm');

    // Add event listener to the form submission
    form.addEventListener('submit', function(event) {
        // Prevent the default form submission behavior
        event.preventDefault();

        // Get the value entered in the query input field
        const query = document.getElementById('query').value;

        // Construct the new action URL based on the query value
        const actionUrl = `/recipes/${query}/search`;

        // Update the form action attribute
        form.action = actionUrl;

        // Submit the form
        form.submit();
    });