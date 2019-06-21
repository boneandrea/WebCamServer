document.addEventListener('DOMContentLoaded', function(){
  const btn=document.querySelector("button");
  btn.addEventListener('click', function(e){
    btn.setAttribute("disabled", true);
    console.log('start to shot');
    fetch('./shot', {
      method: 'GET',
      //      body: 'foo=1&bar=2',
      //      headers: new Headers({'Content-type' : 'application/x-www-form-urlencoded' }),
    })
      .then(function (response) {
        btn.removeAttribute("disabled");
        if (response.status === 200) {
          console.log('done');
          const img=document.querySelector("img");
          img.setAttribute("src", `abc.jpg?${new Date().getTime()}`);
        } else {
          console.log('fail');
        }
      })
      .catch(function (err) {
        btn.removeAttribute("disabled");
        console.log(err);
        console.log('Error Occurred');
      });
  });
}, false);
