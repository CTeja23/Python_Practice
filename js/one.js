function freefall(val, isD){

        if(isD == true){
            const distance = parseFloat(val)
            var t = (2 * distance/9.81) **0.5
            var t = parseFloat(t)

            return t.toFixed(2)
        }
        else{
            const time = parseFloat(val)
            var d = 0.5 * 9.81 * time**2
            return d.toFixed(2)



        }
    }




console.log(freefall(0.45, false))