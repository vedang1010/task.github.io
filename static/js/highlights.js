


    const counterfoot = document.querySelector(".counterfoot");
    let count;
    count=0;
    setInterval(() => {
      if (count == 15000) { 
        clearInterval(count); 
      } else {
        count = count + 100;
        counterfoot.textContent = count + "+";
      }
    }, 42);

    
    const counterintern = document.querySelector(".counterintern");
    let countt = 0;
    setInterval(() => {
      if (countt == 400) {
        clearInterval(countt);
      } else {
        countt = countt + 10;
        counterintern.textContent = countt + "+";
      }
    }, 42);
    const counterinvest = document.querySelector(".counterinvest");
    let counttt = 0;
    setInterval(() => {
      if (counttt == 75) {
        clearInterval(counttt);
      } else {
        counttt = counttt + 1;
        counterinvest.textContent = counttt + "+";
      }
    }, 42);
    const counterstart = document.querySelector(".counterstart");
    let countttt = 40;
    setInterval(() => {
      if (countttt == 120) {
        clearInterval(countttt);
      } else {
        countttt = countttt + 1;
        counterstart.textContent = countttt + "+";
      }
    }, 42);

    

