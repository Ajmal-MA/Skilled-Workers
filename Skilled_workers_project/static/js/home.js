 const ScrollRevealOption = {
        distance:"50px",
        origin:"bottom",
        duration:1000,
    };

    ScrollReveal().reveal(".header_container h2",{
        ...ScrollRevealOption,
    });
     ScrollReveal().reveal(".header_container h1",{
        ...ScrollRevealOption,
        delay:500,
    });
     ScrollReveal().reveal(".header_container p",{
        ...ScrollRevealOption,
        delay:1000,
    });
    ScrollReveal().reveal(".header_btns",{
        ...ScrollRevealOption,
        delay:1500,
    });
    ScrollReveal().reveal(".steps_card", {
        ...ScrollRevealOption,
        interval:500,
    });
    ScrollReveal().reveal(".explore_card", {
        duration:1000,
        interval:500,
    });
    ScrollReveal().reveal(".job_card", {
        ...ScrollRevealOption,
        interval:500,
    });
     ScrollReveal().reveal(".offer_card", {
        ...ScrollRevealOption,
        interval:500,
    });

    const swiper = new Swiper(".swiper", {
        loop:true,
    });