
document.querySelector('form').addEventListener('submit', function(event) {
    var age = document.getElementById('Age').value;
    if (age < 18) {
        alert('Age must be at least 18.');
        event.preventDefault();
    }
});
