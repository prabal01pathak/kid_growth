window.addEventListener("load", () => {
    const image_url = document.querySelector("#id_image_url");
    console.log("image url: ", image_url);
    image_url.addEventListener("change", (e) => {
        console.log(e);
        const image_field = document.querySelector(".readonly img");
        console.log("image field: ", image_field);
        console.log(e.target.vlue);
        image_field.src = e.target.value;
    });
});
