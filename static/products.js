const loadData = () => {
    const scriptElement = document.querySelector('script[data-name="helper"]');
    const messagesJson = JSON.parse(scriptElement.getAttribute('data-message'));
    if (messagesJson) {
        document.getElementById("toaster-title").innerHTML = Object.keys(messagesJson)[0];
        document.getElementById("toaster-description").innerHTML = Object.values(messagesJson)[0];
        let toast = document.querySelector(".toast");
        let progress = document.querySelector(".progress");
        toast.classList.add("active");
        progress.classList.add("active");
        setTimeout(() => {
            console.log('toast')
            toast.classList.remove("active");
        }, 3000)

        setTimeout(() => {
            console.log('toast')
            progress.classList.remove("active");
        }, 3000)
    }
}
window.onload = loadData

