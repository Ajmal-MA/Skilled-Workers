 document.addEventListener("DOMContentLoaded", function () {
        const menuBtn = document.getElementById("menu-btn");
        const navlinks = document.getElementById("nav-links");
        const menuBtnIcon = menuBtn.querySelector("i");
        const loginBtn = document.getElementById("login-btn")
        const loginContainer = document.getElementById("login-container");
        const loginMenu = document.getElementById("login-menu")
        
        menuBtn.addEventListener("click", () => {
            navlinks.classList.toggle("open");
            const isOpen = navlinks.classList.contains("open");
            menuBtnIcon.setAttribute("class", isOpen ? "ri-close-line" : "ri-menu-line");
        });
        navlinks.addEventListener("click", (e) => {
            if (e.target.tagName === "A") {
            navlinks.classList.remove("open");
            menuBtnIcon.setAttribute("class", "ri-menu-line");
            }
        });
        loginBtn.addEventListener("mouseenter" , function () {
            loginMenu.classList.add("open");
        });
        loginBtn.addEventListener("mouseleave" , function (){
            loginMenu.classList.remove("open");
        })
        
    });

