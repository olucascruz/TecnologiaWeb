const inputRadioCandidate = document.getElementById("radio-form-candidate")
const inputRadioRecruiter = document.getElementById("radio-form-recruiter")

const formCandidate = document.getElementById("form-candidate")
const formRecruiter = document.getElementById("form-recruiter")

inputRadioCandidate.click()



if(inputRadioCandidate.checked){
    formCandidate.classList.add("show")
    formRecruiter.classList.remove("show")
}else if(inputRadioRecruiter.checked){
    formCandidate.classList.remove("show")
    formRecruiter.classList.add("show")
}


inputRadioCandidate.addEventListener('change', ()=>{
    if(inputRadioCandidate.checked){
        formCandidate.classList.add("show")
        formRecruiter.classList.remove("show")
        }
    })

inputRadioRecruiter.addEventListener('change', () => {
    if (inputRadioRecruiter.checked) {
        formCandidate.classList.remove('show');
        formRecruiter.classList.add('show');
    }
});
