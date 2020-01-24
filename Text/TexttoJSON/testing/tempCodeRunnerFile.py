what.write(f'fetch("JSON/{u_name}.json")')
        what.write('.then(function(resp) {return resp.json(); })')
        what.write('.then(function(data) {items = data; items.forEach(function(item,index){if (item !== ",") {div = div + item; } }); document.getElementById("react_root").innerHTML =  div; div = "";}); ')