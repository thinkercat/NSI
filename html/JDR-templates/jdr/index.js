
window.addEventListener('load' ,() => {
    function changeHistoryScreen(){
        const body = document.body
        const historyName = document.getElementById("historyName")
        const historyAuthor = document.getElementById("historyAuthor")

        console.log('change history screen')
        body.style.backgroundImage = "url(./futurist_city.png)"
        historyName.innerText = "nom au hasard"
        historyAuthor.innerText = "by claudio"
    }
    window.addEventListener('click', ()=>{
        changeHistoryScreen()
})
})