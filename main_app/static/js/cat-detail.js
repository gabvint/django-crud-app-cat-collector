
const dateInput = document.getElementById('id_date');

const picker = MCDatepicker.create({
    el: '#id_date', 
    dateFormat: 'yyyy-mm-dd', // Set the desired date format
    closeOnBlur: true, // Close picker when clicking outside
    selectedDate: new Date() // Default to today's date
});

dateInput.addEventListener("click", () => {
    picker.open();
})


