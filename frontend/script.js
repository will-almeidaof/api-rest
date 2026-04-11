document.addEventListener("DOMContentLoaded", () => {

    let token = localStorage.getItem("token") || ""
    let user = localStorage.getItem("user") || ""

    const loginScreen = document.getElementById("loginScreen")
    const appScreen = document.getElementById("appScreen")

    function mostrarApp() {
        loginScreen.classList.add("hidden")
        appScreen.classList.remove("hidden")
        document.getElementById("userInfo").innerText = "Logado: " + user
    }

    function mostrarLogin() {
        loginScreen.classList.remove("hidden")
        appScreen.classList.add("hidden")
    }

    window.mostrarRegister = function () {
        document.getElementById("loginBox").classList.add("hidden")
        document.getElementById("registerBox").classList.remove("hidden")
    }

    window.mostrarLoginFromRegister = function () {
        document.getElementById("registerBox").classList.add("hidden")
        document.getElementById("loginBox").classList.remove("hidden")
    }

    window.login = async function () {
        const email = document.getElementById("email").value
        const senha = document.getElementById("senha").value

        const res = await fetch("http://localhost:5000/login", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({email, senha})
        })

        const data = await res.json()

        if (!data.token) {
            showToast("Login Inválido")
            return
        }

        token = data.token
        user = email

        localStorage.setItem("token", token)
        localStorage.setItem("user", user)

        mostrarApp()
    }

    window.logout = function () {
        localStorage.clear()
        token = ""
        user = ""
        mostrarLogin()
    }

    window.listar = async function () {
        const res = await fetch("http://localhost:5000/pessoas", {
            headers: { "Authorization": "Bearer " + token }
        })

        const data = await res.json()

        const lista = document.getElementById("lista")
        lista.innerHTML = ""

        data.forEach(p => {
            const li = document.createElement("li")
            li.innerText = p.name + " - " + p.idade
            lista.appendChild(li)
        })
    }

    window.criar = async function () {
        const name = document.getElementById("nome").value
        const idade = document.getElementById("idade").value

        await fetch("http://localhost:5000/pessoas", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Bearer " + token
            },
            body: JSON.stringify({name, idade})
        })

        listar()
    }

    window.register = async function () {
        const email = document.getElementById("regEmail").value
        const senha = document.getElementById("regSenha").value

        const res = await fetch("http://localhost:5000/register", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({email, senha})
        })

        const data = await res.json()

        if (res.status !== 201) {
            showToast("Erro ao cadastrar")
            return
        }

        showToast("Usuário criado")
        mostrarLoginFromRegister()
    }

    if (token) {
        mostrarApp()
    }

})
function showToast(msg) {
    const toast = document.getElementById("toast")
    toast.innerText = msg
    toast.style.opacity = 1

    setTimeout(() => {
        toast.style.opacity = 0
    }, 2000)
}