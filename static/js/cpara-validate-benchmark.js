// validBench(['CP3d','CP4d','CP5d','CP6d','if_ovc', 'CP1q', 'CP3q', 'CP4q'], ['AYES','AYES','AYES','AYES','AYES','AYES','AYES','AYES'], 'CP1b');


// Healthy Goal 1 >> Benchmark 1
validBench(['CP1q', 'CP2q', 'CP3q', 'CP4q', 'CP5q'], ['AYES','AYES','AYES','AYES','AYES'], 'CP1b');
// Healthy Goal 2 >> Benchmark 2
validBench(['CP6q','CP7q','CP8q','CP9q','CP10q','CP11q','CP12q','CP13q','CP14q'], ['AYES','AYES','AYES','AYES','AYES','AYES','AYES','AYES','AYES'], 'CP2b');

// validBench(['CPhealth15','CPhealth16','CPhealth17'],['AYES','AYES','AYES'],'CPhealth18')
// validBench(['CPhealth15','CPhealth16','CPhealth17'],['AYES','AYES','AYES'],'CPhealth19')
// validBench(['CPhealth15','CPhealth16','CPhealth17'],['AYES','AYES','AYES'],'CPhealth20')

// Healthy Goal 3 >> Benchmark 3
validBench(['CP15q','CP16q','CP17q'],['AYES','AYES','AYES'],'CP3b')
// Healthy Goal 4 >> Benchmark 4
validBench(['CP18q', 'CP19q', 'CP20q', 'CP21q'], ['AYES','AYES', 'AYES','AYES'], 'CP4b');
// Stable: Goal 5:
validBench(['CP22q','CP23q','CP24q'], ['AYES','AYES','AYES'], 'CP5b');
// Safe: Goal 6:Benchmark 6
validBench(['CP25q','CP26q','CP27q','CP28q', 'CP29q'],['AYES','AYES','AYES,ANA','AYES','AYES'],'CP6b')
// Safe: Benchmark 7:
validBench(['CP30q','CP31q'],['AYES','AYES'],'CP7b')
// Safe: Goal 8q
validBench(['CP32q'],['AYES'],'CP8b')
// Schooled: Goal 8: Benachmark 9
validBench(['CP33q','CP34q','CP35q','CP36q'],['AYES','AYES','AYES','AYES'],'CP9b')


validDate('CP2d','CP1d','AYES','ANNO');
// validDate('CP2q','CP1q','ANNO','AYES');
validDate('children_rsk_hiv_assess_date','CP1q','ANNO','AYES');






var benchmarkScore = 0;
$('input[name=p76q],input[name=p75q],input[name=p77q],input[name=p78q],input[name=p79q],input[name=CP_b_total]').attr('readonly', true);

// disable benchmark editing 

// $('input[name=CP1b]').attr('disabled', true);
$('input[name=CP1b]').click(function(){return false;});

// $('input[name=CP2b]').attr('disabled', true);
$('input[name=CP2b]').click(function(){return false;});

// $('input[name=CP3b]').attr('disabled', true);
$('input[name=CP3b]').click(function(){return false;});

// $('input[name=CP4b]').attr('disabled', true);
$('input[name=CP4b]').click(function(){return false;});

// $('input[name=CP5b]').attr('disabled', true);
$('input[name=CP5b]').click(function(){return false;});

// $('input[name=CP6b]').attr('disabled', true);
$('input[name=CP6b]').click(function(){return false;});

// $('input[name=CP7b]').attr('disabled', true);
$('input[name=CP7b]').click(function(){return false;});

// $('input[name=CP8b]').attr('disabled', true);
$('input[name=CP8b]').click(function(){return false;});

// $('input[name=CP9b]').attr('disabled', true);
$('input[name=CP9b]').click(function(){return false;});

// // $('input[name=CP10b]').attr('disabled', true);
// $('input[name=CP10b]').click(function(){return false;});

// // $('input[name=CP11b]').attr('disabled', true);
// $('input[name=CP11b]').click(function(){return false;});

// // $('input[name=CP12b]').attr('disabled', true);
// $('input[name=CP12b]').click(function(){return false;});

// // $('input[name=CP13b]').attr('disabled', true);
// $('input[name=CP13b]').click(function(){return false;});

// // $('input[name=CP14b]').attr('disabled', true);
// $('input[name=CP14b]').click(function(){return false;});

// // $('input[name=CP15b]').attr('disabled', true);
// $('input[name=CP15b]').click(function(){return false;});

// // $('input[name=CP16b]').attr('disabled', true);
// $('input[name=CP16b]').click(function(){return false;});

// // $('input[name=CP17b]').attr('disabled', true);
// $('input[name=CP17b]').click(function(){return false;});


// disable benchmark editing

// benchmark score after change of last benchmark radio
// $('input[name=CP17b], input[name=CP1b], input[name=CP2b], input[name=CP3b], input[name=CP4b], input[name=CP5b], input[name=CP6b], input[name=CP7b], input[name=CP8b], input[name=CP9b], input[name=CP10b], input[name=CP11b], input[name=CP12b], input[name=CP13b], input[name=CP14b], input[name=CP15b], input[name=CP16b], input[name=CP17b]').change(function (e) { 

// $('input[name=CP17b]').change(function (e) {  
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
    if(CP9b === 'AYES'){CP9b = 1;}
    else{CP9b = 0;}
    console.log('benchScore CP9b=> '+CP9b);

    // var CP10b = $('input[name=CP10b]:checked').val();
    // if(CP10b === 'AYES'){CP10b = 1;}
    // else{CP10b = 0;}
    // console.log('benchScore CP10b=> '+CP10b);

    // var CP11b = $('input[name=CP11b]:checked').val();
    // if(CP11b === 'AYES'){CP11b = 1;}
    // else{CP11b = 0;}
    // console.log('benchScore CP11b=> '+CP11b);

    // var CP12b = $('input[name=CP12b]:checked').val();
    // if(CP12b === 'AYES'){CP12b = 1;}
    // else{CP12b = 0;}
    // console.log('benchScore CP12b=> '+CP12b);

    // var CP13b = $('input[name=CP13b]:checked').val();
    // if(CP13b === 'AYES'){CP13b = 1;}
    // else{CP13b = 0;}
    // console.log('benchScore CP13b=> '+CP13b);

    // var CP14b = $('input[name=CP14b]:checked').val();
    // if(CP14b === 'AYES'){CP14b = 1;}
    // else{CP14b = 0;}
    // console.log('benchScore CP14b=> '+CP14b);

    // var CP15b = $('input[name=CP15b]:checked').val();
    // if(CP15b === 'AYES'){CP15b = 1;}
    // else{CP15b = 0;}
    // console.log('benchScore CP15b=> '+CP15b);

    // var CP16b = $('input[name=CP16b]:checked').val();
    // if(CP16b === 'AYES'){CP16b = 1;}
    // else{CP16b = 0;}
    // console.log('benchScore CP16b=> '+CP16b);

    // var CP17b = $('input[name=CP17b]:checked').val();
    // if(CP17b === 'AYES'){CP17b = 1;}
    // else{CP17b = 0;}
    // console.log('benchScore CP17b=> '+CP17b);
    
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
    // bench_array.push( CP10b );
    // bench_array.push( CP11b );
    // bench_array.push( CP12b );
    // bench_array.push( CP13b );
    // bench_array.push( CP14b );
    // bench_array.push( CP15b );
    // bench_array.push( CP16b );
    // bench_array.push( CP17b );
    $('input[name=CP74q]').val(benchmarkScore); //  Overall number of points

    $('input[name=p75q]').val(healthScore); // Healthy Domain
    $('input[name=p76q]').val(stableScore); // Stable Domain
    $('input[name=p77q]').val(safeScore); // Safe Domain
    $('input[name=p78q]').val(schoolScore); // Schooled Domain
    $('input[name=p79q]').val(healthScore+stableScore+safeScore+schoolScore); //Total Score
    $('input[name=CP_b_total]').val(healthScore+stableScore+safeScore+schoolScore); //Total Score
    $('input[name=bench_array]').val(JSON.stringify(bench_array));
    console.log('benchmark_score => '+JSON.stringify(bench_array));


    
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

function validDate(dateFieldName, radioToCheck, rightValue, wrongValue) {
    $('input[name='+dateFieldName+']').attr('disabled', true);
	$('input[name='+radioToCheck+']').change(function(){
		var valu = $(this).val();
		if(valu === rightValue){
			$('input[name='+dateFieldName+']').val('');
			$('input[name='+dateFieldName+']').attr('disabled', true);
			$('input[name='+dateFieldName+']').removeAttr('required');
			$('input[name='+dateFieldName+']').attr('data-parsley-required', false);
			$('input[name='+dateFieldName+']').removeClass('parsley-error');
            var dpid = $('input[name='+dateFieldName+']').attr('data-parsley-id');
            $('#parsley-id-'+dpid).addClass('hidden');
		}else if(valu === wrongValue){
			$('input[name='+dateFieldName+']').attr('data-parsley-required', true);
			$('input[name='+dateFieldName+']').val('');
			$('input[name='+dateFieldName+']').removeAttr('disabled');
		}
	});
}
// end----------------CORE----------------