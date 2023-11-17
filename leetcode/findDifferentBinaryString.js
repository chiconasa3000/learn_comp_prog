
function dec2bin(number, maxi, mini, size_bit){
    let acum = 0;
    let lit_bin = "";
    let temp_acum = 0;

    if(number < maxi && number > mini){
        // casting decimal number to binary
        for(let i=size_bit-1; i>=0; i--){
            temp_acum += (2**i);
            // update literal_binary
            lit_bin += (temp_acum <= number) ? "1":"0";
            // update acumulator
            acum += (temp_acum <= number) ? temp_acum:0;            
            temp_acum = acum;
        }

        if(!(nums.includes(lit_bin))){
            return lit_bin;
        }
    }
}

function ff(nums){

    const size_bit = nums[0].length;
    const max_bin_num = 2**size_bit;
    const min_bin_num = 0;
    // when it has only one bit 
    if(size_bit == 1){
        if(nums[0]==0)
            return 1;
        else
            return 0;
    }

    // iterate on every binary number
    for(const bin_number of nums){

        let curr_binary = Number("0b" + bin_number);
        let next_binary = curr_binary + 1;
        let prev_binary = curr_binary - 1;
        
        let acum = 0;
        let lit_bin = "";
        let temp_acum = 0;

        // next_binary number as a literal binary number
        const exist_prev_bin = dec2bin(prev_binary, max_bin_num, min_bin_num, size_bit);
        const exist_next_bin = dec2bin(next_binary, max_bin_num, min_bin_num, size_bit);
        console.log("exist_next_bin: ",exist_next_bin);
        console.log("exist_prev_bin: ",exist_prev_bin);

        if(exist_prev_bin){
            return exist_prev_bin;
        }
        if(exist_next_bin){
            return exist_next_bin;
        }
        

        // previous_binary number as a literal binary number
        
    }
}
let nums = ["111","011","001"]
console.log(`There is no: ${ff(nums)}`);
