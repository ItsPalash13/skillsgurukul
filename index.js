var animation = bodymovin.loadAnimation({
  container: document.getElementById('animContainer'),
  renderer: 'svg',
  loop: true,
  autoplay: true,
  path: 'https://assets9.lottiefiles.com/packages/lf20_ncpnijkz.json' // lottie file path
})

function fun1(p,c){
bodymovin.loadAnimation({
  container: document.getElementById(c),
  renderer: 'svg',
  loop: true,
  autoplay: true,
  path: p // lottie file path
})
}


fun1("https://assets4.lottiefiles.com/private_files/lf30_gcroxmlt.json",'animContainer2')
fun1("https://assets2.lottiefiles.com/packages/lf20_fq7pwzey.json",'animContainer1')
fun1("https://assets3.lottiefiles.com/packages/lf20_3bybkzbo.json",'animContainer3')
fun1("https://assets2.lottiefiles.com/packages/lf20_wcj1op19.json",'animContainer4')

