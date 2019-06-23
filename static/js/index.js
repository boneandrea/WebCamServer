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
        console.log(response);
        if (response.status === 200) {
          console.log('done');
        } else {
          console.log('fail');
        }
        return response.json();
      })
      .then((data) => {
        console.log( data );
        const img=document.querySelector("img");
        const img_base="https://knuckle-images.s3-ap-northeast-1.amazonaws.com";
        img.setAttribute("src", `${img_base}/${data.filename}`);

      })
      .catch(function (err) {
        btn.removeAttribute("disabled");
        console.log(err);
        console.log('Error Occurred');
      });
  });
}, false);
