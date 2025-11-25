const nameSelect = document.getElementById('name');
const checkBtn = document.getElementById('check');
const closeBtn = document.getElementById('close');
const popup = document.getElementById("popup");
const myName = document.getElementById('my-name');
const personName = document.getElementById('person-name');
const namesPath = "./js/names.json";
let obj = null;

checkBtn.addEventListener("click", displayAnswer);
closeBtn.addEventListener("click", closePopup);
popup.addEventListener("click", e => {
    if(e.target === popup) closePopup();
});

function populateSelect() {
    fetch(namesPath)
    .then(response => {
        if (response.ok)           
            return response.json();
        else
            throw new Error("Coś poszło nie tak...");
    })
    .then(data => {
        obj = data;
        const names = Object.keys(data);

        names.forEach(name => {
            option = document.createElement('option');
            option.value = name;
            option.innerText = name;
            nameSelect.appendChild(option);
        });
    })
    .catch(err => {
        console.log(err);
    });
}

function displayAnswer() {
    currentSelection = nameSelect.value;

    if (currentSelection !== "..." || !obj) {
        const myNameText = currentSelection;
        const personNameText = obj[myNameText];

        myName.innerText = myNameText;
        personName.innerText = personNameText;

        popup.classList.add("show");
    }    
}

function closePopup() {
    popup.classList.remove("show");
}

populateSelect();