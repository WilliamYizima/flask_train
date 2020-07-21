const pupil = document.querySelector(".pupil");

document.addEventListener("mousemove", (e) => {
	let x = e.clientX * 100 / window.innerWidth - 50;
	let y = e.clientY * 100 / window.innerHeight - 50;

	pupil.style.left = x + "%";
	pupil.style.top = y + "%";
})

