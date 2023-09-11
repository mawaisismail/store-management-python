const successMessage = {
    'success': "This is a success message",
}
const failedMessage = {
    'Failed': "Some thing went wrong",
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const loadData = (message = null) => {
    const scriptElement = document.querySelector('script[data-name="helper"]');
    if (Object.keys(message).length) {
        document.getElementById("toaster-title").innerHTML = Object.keys(message)[0];
        document.getElementById("toaster-description").innerHTML = Object.values(message)[0];
        let toast = document.querySelector(".toast");
        let progress = document.querySelector(".progress");
        toast.classList.add("active");
        progress.classList.add("active");
        setTimeout(() => {
            toast.classList.remove("active");
        }, 1000)

        setTimeout(() => {
            progress.classList.remove("active");
        }, 1000)
    }
}

function addProductToCart(id) {
    let csrftoken = getCookie('csrftoken');
    fetch(`http://localhost:8000/products/add_to_cart/${id}`, {
        method: "POST",
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            "X-CSRFToken": csrftoken
        },
    }).then((response) => {
        if (!response.ok) {
            return loadData(failedMessage);
        }
        return loadData(successMessage);
    }).catch((e) => {
        console.log("Network Error:", e);
        loadData(failedMessage);
    });

}
