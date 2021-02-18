
 function my_hamming_dna(param_1,param_2) {
     list_a = param_1.split("");
     list_b = param_2.split("");
     count = 0;
     if(param_1 == param_2){
         count = 0;
     }
     if(param_1.length != param_2.length){
         count = -1;
     }
     if(param_1.length == param_2.length){
         for (let i = 0; i < param_1.length; i++) {
             if(list_a[i] != list_b[i]){
                 count++;
             }
         }
     }
     return count
     // console.log(count);
 }
 // my_hamming_dna("ACCAGGG","ACTATGG");
