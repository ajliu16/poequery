"use strict";
let items = [];
let div = "";
let divsave = []
fetch("JSON/Uniques.json").then(function(resp)
{return resp.json(); }).then(function(data)
{items = data; items.forEach(function(item,index){if (item !== ",")
{div = div + item; divsave.push(item) } });
document.getElementById("react_root").innerHTML =  div; div = "";});

var delayTimer;
document.getElementById('query').addEventListener('keyup',function(e){
	if (e.which == 13) this.blur();
});
function search() {
    clearTimeout(delayTimer);
    delayTimer = setTimeout(function() {
        let text = document.getElementById("query").value.toLowerCase();
        text = text.replace("'", "");
        divsave.forEach(function(item,index){
        {let x = item.toLowerCase(); x = x.replace("'", "");
        let indexit = x.indexOf(text);
        if (indexit !== -1) {div = div + item; } } });
        document.getElementById("react_root").innerHTML =  div; div = "";
        reset();
    }, 250	);
};

function reslick(){
$(document).ready(function(){
    $('.unique_filters2').slick();
  });

$('.unique_filters2').slick({
dots: false,
arrows: true,
infinite: false,
speed: 300,
slidesToShow: 6,
slidesToScroll: 6,
responsive: [
    {
    breakpoint: 1024,
    settings: {
        slidesToShow: 4,
        slidesToScroll: 4,
        infinite: false,
        dots: false
    }
    },
    {
    breakpoint: 600,
    settings: {
        slidesToShow: 4,
        slidesToScroll: 4
    }
    },
    {
    breakpoint: 480,
    settings: {
        slidesToShow: 3,
        slidesToScroll: 3
    }
    }
]
});
};

function reslick2(){
$(document).ready(function(){
    $('.unique_filters3').slick();
  });

$('.unique_filters3').slick({
dots: false,
arrows: true,
infinite: false,
speed: 300,
slidesToShow: 6,
slidesToScroll: 6,
responsive: [
    {
    breakpoint: 1024,
    settings: {
        slidesToShow: 4,
        slidesToScroll: 4,
        infinite: false,
        dots: false
    }
    },
    {
    breakpoint: 600,
    settings: {
        slidesToShow: 4,
        slidesToScroll: 4
    }
    },
    {
    breakpoint: 480,
    settings: {
        slidesToShow: 3,
        slidesToScroll: 3
    }
    }
]
});
};


function get_json(x) {
	if(x==='Weapons'){
		$('.unique_filters2').slick("unslick");
		document.getElementById("click_filter").innerHTML =  `<li class="filters" onclick="return get_json('Swords');"><a>Swords</a></li><li class="filters" onclick="return get_json('Axes');"><a href="">Axes</a></li><li class="filters" onclick="return get_json('Maces');"><a href="">Maces</a></li><li class="filters" onclick="return get_json('Daggers');"><a href="">Daggers</a></li><li class="filters" onclick="return get_json('Claws');"><a href="">Claws</a></li><li class="filters" onclick="return get_json('Staves');"><a href="">Staves</a></li><li class="filters" onclick="return get_json('Wands');"><a href="">Wands</a></li><li class="filters2" onclick="return get_json('Bows');"><a href="">Bows</a></li>`;
    document.getElementById('click_filter2').innerHTML = '';
    
		reslick();

	} else if (x==='AllArmours') {
		$('.unique_filters2').slick("unslick");
		document.getElementById("click_filter").innerHTML =  `<li class="filters" onclick="return get_json('BodyArmours');"><a href="">Body Armour</a></li><li class="filters" onclick="return get_json('Helmets');"><a href="">Helmets</a></li><li class="filters" onclick="return get_json('Gloves');"><a href="">Gloves</a></li><li class="filters" onclick="return get_json('Boots');"><a href="">Boots</a></li><li class="filters" onclick="return get_json('Shields');"><a href="">Shields</a></li><li class="filters" onclick="return get_json('Quivers');"><a href="">Quivers</a></li>`;
		document.getElementById('click_filter2').innerHTML = ''; 
		reslick();
	};
	if (x==='Uniques' || x === 'Flasks' || x === 'Maps' || x==='Jewels'){
		$('.unique_filters2').slick("unslick");
		document.getElementById("click_filter").innerHTML = '';
		document.getElementById('click_filter2').innerHTML = ''; 
		reslick();
	};
	if (x ==='Quivers'){
		$('.unique_filters3').slick("unslick");
		document.getElementById('click_filter2').innerHTML = ''; 
		reslick2();
	}
	if (x==='Swords' || x==='Axes' || x==='Maces' || x==='Daggers' || x==='Claws' || x==='Staves' || x==='Wands' || x==='Bows') {
		$('.unique_filters3').slick("unslick");
		document.getElementById('click_filter2').innerHTML = `<li class="filters" onclick="return get_json('${x}_Level_Requirement');"><a href="">Level Req</a></li><li class="filters" onclick="return get_json('${x}_Dps');"><a href="">Dps</a></li><li class="filters" onclick="return get_json('${x}_Attack_Speed');"><a href="">Attack Speed</a></li><li class="filters2" onclick="return get_json('${x}_Critical_Chance');"><a href="">Crit Chance</a></li>`;
		reslick2();
	};
	if (x ==='BodyArmours' || x ==='Helmets' || x ==='Gloves' || x ==='Boots' || x ==='Shields'){
		$('.unique_filters3').slick("unslick");
		document.getElementById('click_filter2').innerHTML = `<li class="filters" onclick="return get_json('${x}_Level_Requirement');"><a href="">Level Req</a></li><li class="filters" onclick="return get_json('${x}_Armour');"><a href="">Armour</a></li><li class="filters" onclick="return get_json('${x}_Evasion');"><a href="">Evasion</a></li><li class="filters2" onclick="return get_json('${x}_Energy_Shield');"><a href="">Energy Shield</a></li>`;
		reslick2();
	};
	divsave = [];
	fetch(`JSON/${x}.json`).then(function(resp)
	{return resp.json(); }).then(function(data)
	{items = data; items.forEach(function(item,index){if (item !== ",")
	{div = div + item; divsave.push(item) } });
  document.getElementById("react_root").innerHTML =  div; div = "";});
  if (x=='Weapons'){
    reset(1000);
  } else {
    reset();
  };
	return false;
};

var scroll = document.getElementById('scroll_top');

window.onscroll = function(){scrolling()};

function scrolling(){
	if (document.body.scrollTop > 1000 || document.documentElement.scrollTop > 1000) {
		scroll.style.display = 'block';
	} else {
		scroll.style.display = 'none';
	};
};

function click_top() {
	document.body.scrollTop = 0;
	document.documentElement.scrollTop = 0;
}
function reset(delay = 600) {
  setTimeout(function(){
    var lazyImages = [].slice.call(document.querySelectorAll("img.lazy"));
    if ("IntersectionObserver" in window) {
      let lazyImageObserver = new IntersectionObserver(function(entries, observer) {
        entries.forEach(function(entry) {
          if (entry.isIntersecting) {
            let lazyImage = entry.target;
            lazyImage.src = lazyImage.dataset.src;
            lazyImage.srcset = lazyImage.dataset.srcset;
            lazyImage.classList.remove("lazy");
            lazyImageObserver.unobserve(lazyImage);
          }
        });
      });
      lazyImages.forEach(function(lazyImage) {
        lazyImageObserver.observe(lazyImage);
      });
    }
  }, delay);
};
reset(1200);