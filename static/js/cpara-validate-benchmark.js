jQuery(document).ready(function()
{

markBenchmark('CP23q_b_1', false)

markBenchmark('CP23q_b_2', false)

markBenchmark('CP23q_b_3', false)

markBenchmark('cp58q', false)

// Benchmark 1
validBench(['CP1q', 'CP2q', 'CP3q', 'CP4q', 'CP5q'], ['AYES','AYES','AYES','AYES','AYES'], 'CP1b');
// Benchmark 2
validBench(['CP6q','CP7q','CP8q','CP9q','CP10q','CP11q','CP12q','CP13q','CP14q'], ['AYES','AYES','AYES','AYES','AYES','AYES','AYES','AYES','AYES'], 'CP2b');

// Healthy Goal 3 >> Benchmark 3
validBench(['CP23q_b_1','CP23q_b_2','CP23q_b_3'],['AYES','AYES','AYES'],'CP3b')
// Healthy Goal 4 >> Benchmark 4
validBench(['CP18q', 'CP19q', 'CP20q', 'CP21q'], ['AYES','AYES', 'AYES','AYES'], 'CP4b');
// Stable: Goal 5: >> Benchmark 5
validBench(['CP22q','CP23q','CP24q'], ['AYES','AYES','AYES'], 'CP5b');
// Safe: Goal 6 >> Benchmark 6
validBench(['CP25q','CP26q','CP26q_ctl','cp58q','CP28q', 'CP29q'],['AYES','AYES','AYES,ANA','AYES','AYES', 'AYES'],'CP6b')
// Safe: Benchmark 7:   
validBench(['CP30q','CP31q'],['AYES','AYES'],'CP7b')
// Safe: Goal 8  >> Benchmark 8
validBench(['CP32q'],['AYES'],'CP8b')
// Schooled: Goal 8: Benachmark 9
validBench(['CP33q','CP34q','CP35q','CP36q'],['AYES','AYES','AYES','AYES'],'CP9b')

});

validDate('CP2d','CP1d','AYES','ANNO');

validDate('children_rsk_hiv_assess_date','CP1q','ANNO','AYES');






var benchmarkScore = 0;
$('input[name=p76q],input[name=p75q],input[name=p77q],input[name=p78q],input[name=p79q],input[name=CP_b_total]').attr('readonly', true);

// disable benchmark editing 

// // $('input[name=CP1b]').attr('disabled', true);
// $('input[name=CP1b]').click(function(){return false;});

// // $('input[name=CP2b]').attr('disabled', true);
// $('input[name=CP2b]').click(function(){return false;});

// // $('input[name=CP3b]').attr('disabled', true);
// $('input[name=CP3b]').click(function(){return false;});

// // $('input[name=CP4b]').attr('disabled', true);
// $('input[name=CP4b]').click(function(){return false;});

// // $('input[name=CP5b]').attr('disabled', true);
// $('input[name=CP5b]').click(function(){return false;});

// // $('input[name=CP6b]').attr('disabled', true);
// $('input[name=CP6b]').click(function(){return false;});

// // $('input[name=CP7b]').attr('disabled', true);
// $('input[name=CP7b]').click(function(){return false;});

// // $('input[name=CP8b]').attr('disabled', true);
// $('input[name=CP8b]').click(function(){return false;});

// // $('input[name=CP9b]').attr('disabled', true);
// $('input[name=CP9b]').click(function(){return false;});


$('input[type=radio]').change(function (e) {  
    var CP1b = $('input[name=CP1b]:checked').val();
    if(CP1b === 'AYES'){CP1b = 1;}
    else{CP1b = 0;}
    console.log('benchScore CP1b=> '+CP1b);

    var CP2b = $('input[name=CP2b]:checked').val();
    if(CP2b === 'AYES'){CP2b = 1;}
    else{CP2b = 0;}
    console.log('benchScore CP2b=> '+CP2b);

    var CP3b = $('input[name=CP3b]:checked').val();
    if(CP3b === 'AYES'){CP3b = 1;}
    else{CP3b = 0;}
    console.log('benchScore CP3b=> '+CP3b);

    var CP4b = $('input[name=CP4b]:checked').val();
    if(CP4b === 'AYES'){CP4b = 1;}
    else{CP4b = 0;}
    console.log('benchScore CP4b=> '+CP4b);

    var CP5b = $('input[name=CP5b]:checked').val();
    if(CP5b === 'AYES'){CP5b = 1;}
    else{CP5b = 0;}
    console.log('benchScore CP5b=> '+CP5b);

    var CP6b = $('input[name=CP6b]:checked').val();
    if(CP6b === 'AYES'){CP6b = 1;}
    else{CP6b = 0;}
    console.log('benchScore CP6b=> '+CP6b);

    var CP7b = $('input[name=CP7b]:checked').val();
    if(CP7b === 'AYES'){CP7b = 1;}
    else{CP7b = 0;}
    console.log('benchScore CP7b=> '+CP7b);

    var CP8b = $('input[name=CP8b]:checked').val();
    if(CP8b === 'AYES'){CP8b = 1;}
    else{CP8b = 0;}
    console.log('benchScore CP8b=> '+CP8b);

    var CP9b = $('input[name=CP9b]:checked').val(); 
    if(CP9b === 'AYES'){CP9b = 0;}
    else{CP9b = 1;}
    console.log('benchScore CP9b=> '+CP9b);



    
    benchmarkScore =  parseFloat(CP1b) + parseFloat(CP2b) + parseFloat(CP3b) + parseFloat(CP4b) + parseFloat(CP5b) + parseFloat(CP6b) + parseFloat(CP7b) + parseFloat(CP8b) + parseFloat(CP9b) // + parseFloat(CP10b) + parseFloat(CP11b) + parseFloat(CP12b) + parseFloat(CP13b) + parseFloat(CP14b) + parseFloat(CP15b) + parseFloat(CP16b) + parseFloat(CP17b);
    healthScore = parseFloat(CP1b)+parseFloat(CP2b)+parseFloat(CP3b)+parseFloat(CP4b)
    stableScore = parseFloat(CP5b)
    safeScore = parseFloat(CP6b)+parseFloat(CP7b)+parseFloat(CP8b)
    schoolScore = parseFloat(CP9b)

    console.log('TOTAL benchScore=> '+benchmarkScore);
    
    var bench_array = [];
    
    bench_array.push( CP1b );
    bench_array.push( CP2b );
    bench_array.push( CP3b );
    bench_array.push( CP4b );
    bench_array.push( CP5b );
    bench_array.push( CP6b );
    bench_array.push( CP7b );
    bench_array.push( CP8b );
    bench_array.push( CP9b );
   
    $('input[name=CP74q]').val(benchmarkScore); //  Overall number of points

    total_score = healthScore+stableScore+safeScore+schoolScore


    $('input[name=p75q]').val(healthScore); // Healthy Domain
    $('input[name=p76q]').val(stableScore); // Stable Domain
    $('input[name=p77q]').val(safeScore); // Safe Domain
    $('input[name=p78q]').val(schoolScore); // Schooled Domain
    $('input[name=p79q]').val(total_score); //Total Score
    
    $('input[name=CP_b_total]').val(total_score); //Total Score
    $('input[name=bench_array]').val(JSON.stringify(bench_array));
    console.log('benchmark_score => '+JSON.stringify(bench_array));
    
    

    if(total_score <= 4){
        
        $('#score_key_1').addClass('bg-primary p-5')
        $('#score_key_2, #score_key_3, #score_key_4').removeClass('bg-primary')
        $('#score_key_2, #score_key_3, #score_key_4').addClass('bg-default')
    }
    else if(total_score >= 5 && total_score <= 7) {
        $('#score_key_2').addClass('bg-primary p-5')

        $('#score_key_1').removeClass('bg-primary')
        $('#score_key_3').removeClass('bg-primary') 
        $('#score_key_4').removeClass('bg-primary') 
        
        $('#score_key_1').addClass('bg-default')
        $('#score_key_3').addClass('bg-default') 
        $('#score_key_4').addClass('bg-default') 
      
    }
    else if(total_score == 8) {
        $('#score_key_3').addClass('bg-primary p-5')
        $('#score_key_1, #score_key_2, #score_key_4').removeClass('bg-primary')
        $('#score_key_1, #score_key_2, #score_key_4').addClass('bg-default')
    }
    else {
       
            $('#score_key_4').addClass('bg-primary p-5')
            $('#score_key_1, #score_key_3, #score_key_2').removeClass('bg-primary')
            $('#score_key_1, #score_key_3, #score_key_2').addClass('bg-default')
        
    }




    
});

// benchmark score after change of last benchmark radio



// ----------------CORE----------------
function validBenchOLD(arrayOfInputsToCheck, arrayOfExpectedValues, idOfBenchmarkQn) {
    // $('input[name='+idOfBenchmarkQn+']').attr('disabled', true);

    // prevent manual benchmark ticking
    $('input[name='+idOfBenchmarkQn+']').change(function() {
        // var vf = $(this).val();
        // if(vf == 'AYES'){
        //     $('input[name='+idOfBenchmarkQn+'][value=ANNO]').prop("checked", true);
        // }else if(vf =='ANNO'){
        //     $('input[name='+idOfBenchmarkQn+'][value=ANNO]').prop("checked", true);
        // }
    });
    // prevent manual benchmark ticking

    var valToMatch = arrayOfInputsToCheck.length;
    var actualValNo = 1;
    $.each(arrayOfInputsToCheck, function (inde, inputName) {
        $('input[name='+inputName+']').change(function() {
            var thisval = $(this).val();
            if(thisval !== arrayOfExpectedValues[inde]){
                // $('input[name='+idOfBenchmarkQn+']').removeAttr('disabled');
                $('input[name='+idOfBenchmarkQn+'][value=ANNO]').prop("checked", true);
                // $('input[name='+idOfBenchmarkQn+']').attr('disabled', true);
                if(thisval === arrayOfExpectedValues[inde]){
                    actualValNo = actualValNo + 1;
                }else{
                    actualValNo = actualValNo;
                    if(actualValNo<1){
                        actualValNo = 1;
                    }
                }
            }else{

                if(actualValNo == valToMatch){
                    $('input[name='+idOfBenchmarkQn+']').removeAttr('disabled');
                    $('input[name='+idOfBenchmarkQn+'][value=AYES]').prop("checked", true);
                    $('input[name='+idOfBenchmarkQn+']').attr('disabled', true);
                    //update benchmark score
                    // benchmarkScore = benchmarkScore + 1
                    // $('input[name=CP74q]').val(benchmarkScore);
                    // console.log("added benchmark + 1 = "+benchmarkScore);
                    //update benchmark score
                }else{
                    $('input[name='+idOfBenchmarkQn+']').removeAttr('disabled');
                    $('input[name='+idOfBenchmarkQn+'][value=ANNO]').prop("checked", true);
                    $('input[name='+idOfBenchmarkQn+']').attr('disabled', true);
                    // console.log('2nd NOone works');
                    if(thisval === arrayOfExpectedValues[inde]){
                        actualValNo = actualValNo + 1;
                    }else{
                        actualValNo = actualValNo;
                        if(actualValNo<1){
                            actualValNo = 1;
                        }
                    }
                }
                // alert(actualValNo+'/'+valToMatch);
            }
        });
        
    });


}


function validBench(arrayOfInputsToCheck, arrayOfExpectedValues, idOfBenchmarkQn) {
    $('input').change(function () {
        markBenchmark(idOfBenchmarkQn, false);
        var proceed = 0;
        
        $.each(arrayOfInputsToCheck, function (inx, inpt) { 
            var thisval = $('input[name='+inpt+']:checked').val();
            if(arrayOfExpectedValues[inx].split(',').length > 1) {
                // console.log(arrayOfExpectedValues[inx], arrayOfExpectedValues[inx][1])
                if(thisval == arrayOfExpectedValues[inx].split(',')[0] || thisval == arrayOfExpectedValues[inx].split(',')[1] ){
                    proceed += 1;
                    return proceed
                }
            }
            else {
                if(thisval == arrayOfExpectedValues[inx]){
                    proceed += 1;
                    return proceed
                }
            }
           
           return
        });
        
        if(proceed == arrayOfInputsToCheck.length){
            markBenchmark(idOfBenchmarkQn, true);
        }else{
            markBenchmark(idOfBenchmarkQn, false);
        }
    })
}



function markBenchmark(benchmarkId, passOrFail) {
    console.log('marking benchmark' +benchmarkId)
    if(passOrFail){
        // $('input[name="'+benchmarkId+'"][value="AYES"]').attr('checked', true);
        $('input[name='+benchmarkId+']').removeAttr('disabled');
        $('input[name='+benchmarkId+'][value=AYES]').prop("checked", true);
        $('input[name='+benchmarkId+']').attr('disabled', true);
    }else{
        $('input[name='+benchmarkId+']').removeAttr('disabled');
        $('input[name='+benchmarkId+'][value=ANNO]').prop("checked", true);
        $('input[name='+benchmarkId+']').attr('disabled', true);
    }
}
// validDate('CP2d','CP1d','AYES','ANNO');
function validDate(dateFieldName, radioToCheck, rightValue, wrongValue) {
    // $('input[name='+dateFieldName+']').attr('disabled', true);
	$('input[name='+radioToCheck+']').change(function(){
		var valu = $(this).val();
		if(valu === rightValue){
			$('input[name='+dateFieldName+']').datepicker().val('1900-01-01');
			// $('input[name='+dateFieldName+']').attr('readonly', true);
			$('input[name='+dateFieldName+']').removeAttr('required');
			$('input[name='+dateFieldName+']').attr('data-parsley-required', false);
			// $('input[name='+dateFieldName+']').removeClass('parsley-error');
            // var dpid = $('input[name='+dateFieldName+']').attr('data-parsley-id');
            // $('#parsley-id-'+dpid).addClass('hidden');
		}else if(valu === wrongValue){
            $('input[name='+dateFieldName+']').attr('readonly', false);
			$('input[name='+dateFieldName+']').attr('data-parsley-required', true);
			$('input[name='+dateFieldName+']').val('');
			$('input[name='+dateFieldName+']').removeAttr('disabled');
		}
	});
}
// end----------------CORE----------------