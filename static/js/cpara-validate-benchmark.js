// validBench(['cp3d','cp4d','cp5d','cp6d','if_ovc', 'cp1q', 'cp3q', 'cp4q'], ['AYES','AYES','AYES','AYES','AYES','AYES','AYES','AYES'], 'cp1b');


// Healthy Goal 1 >> Benchmark 1
validBench(['cphealth1', 'cphealth2', 'cphealth3', 'cphealth4', 'cphealth5'], ['AYES','AYES','AYES','AYES','AYES'], 'cp1b');
// Healthy Goal 2 >> Benchmark 2
validBench(['cphealth6','cphealth7','cphealth8','cphealth9','cphealth10','cphealth11','cphealth12','cphealth13','cphealth14'], ['AYES','AYES','AYES','AYES','AYES','AYES','AYES','AYES','AYES'], 'cp2b');
// Healthy Goal 3 >> Benchmark 3
validBench(['cphealth18','cphealth19','cphealth20'],['AYES','AYES','AYES'],'cp3b')
// Healthy Goal 4 >> Benchmark 4
validBench(['cphealth21', 'cphealth22', 'cphealth23', 'cphealth24'], ['AYES','AYES', 'AYES','AYES'], 'cp4b');
// Stable: Goal 5:
validBench(['cpstable1','cpstable2','cpstable3'], ['AYES','AYES','AYES'], 'cp5b');
// Safe: Goal 6:Benchmark 6
validBench(['cpsafe1','cpsafe2','cpsafe3','cpsafe4','cpsafe5'],['AYES','AYES','AYES','AYES', 'AYES'],'cp6b')
// Safe: Benchmark 7:
validBench(['cpsafe8','cpsafe9'],['AYES','AYES'],'cp7b')
// Safe: Goal 8:
validBench(['cpsafe10'],['AYES'],'cp8b')
// Schooled: Goal 8: Benachmark 9
validBench(['cpschool1','cpschool2','cpschool3','cpschool4'],['AYES','AYES','AYES','AYES'],'cp9b')


validDate('cp2d','cp1d','AYES','ANNO');
// validDate('cp2q','cp1q','ANNO','AYES');
validDate('children_rsk_hiv_assess_date','cp1q','ANNO','AYES');

var benchmarkScore = 0;
$('input[name=cp74q],input[name=cp75q],input[name=cp76q],input[name=cp77q],input[name=cp78q],input[name=cp79q]').attr('readonly', true);

// disable benchmark editing 

// $('input[name=cp1b]').attr('disabled', true);
$('input[name=cp1b]').click(function(){return false;});

// $('input[name=cp2b]').attr('disabled', true);
$('input[name=cp2b]').click(function(){return false;});

// $('input[name=cp3b]').attr('disabled', true);
$('input[name=cp3b]').click(function(){return false;});

// $('input[name=cp4b]').attr('disabled', true);
$('input[name=cp4b]').click(function(){return false;});

// $('input[name=cp5b]').attr('disabled', true);
$('input[name=cp5b]').click(function(){return false;});

// $('input[name=cp6b]').attr('disabled', true);
$('input[name=cp6b]').click(function(){return false;});

// $('input[name=cp7b]').attr('disabled', true);
$('input[name=cp7b]').click(function(){return false;});

// $('input[name=cp8b]').attr('disabled', true);
$('input[name=cp8b]').click(function(){return false;});

// $('input[name=cp9b]').attr('disabled', true);
$('input[name=cp9b]').click(function(){return false;});

// // $('input[name=cp10b]').attr('disabled', true);
// $('input[name=cp10b]').click(function(){return false;});

// // $('input[name=cp11b]').attr('disabled', true);
// $('input[name=cp11b]').click(function(){return false;});

// // $('input[name=cp12b]').attr('disabled', true);
// $('input[name=cp12b]').click(function(){return false;});

// // $('input[name=cp13b]').attr('disabled', true);
// $('input[name=cp13b]').click(function(){return false;});

// // $('input[name=cp14b]').attr('disabled', true);
// $('input[name=cp14b]').click(function(){return false;});

// // $('input[name=cp15b]').attr('disabled', true);
// $('input[name=cp15b]').click(function(){return false;});

// // $('input[name=cp16b]').attr('disabled', true);
// $('input[name=cp16b]').click(function(){return false;});

// // $('input[name=cp17b]').attr('disabled', true);
// $('input[name=cp17b]').click(function(){return false;});


// disable benchmark editing

// benchmark score after change of last benchmark radio
// $('input[name=cp17b], input[name=cp1b], input[name=cp2b], input[name=cp3b], input[name=cp4b], input[name=cp5b], input[name=cp6b], input[name=cp7b], input[name=cp8b], input[name=cp9b], input[name=cp10b], input[name=cp11b], input[name=cp12b], input[name=cp13b], input[name=cp14b], input[name=cp15b], input[name=cp16b], input[name=cp17b]').change(function (e) { 

// $('input[name=cp17b]').change(function (e) {  
$('input[type=radio]').change(function (e) {  
    var cp1b = $('input[name=cp1b]:checked').val();
    if(cp1b === 'AYES'){cp1b = 1;}
    else{cp1b = 0;}
    console.log('benchScore cp1b=> '+cp1b);

    var cp2b = $('input[name=cp2b]:checked').val();
    if(cp2b === 'AYES'){cp2b = 1;}
    else{cp2b = 0;}
    console.log('benchScore cp2b=> '+cp2b);

    var cp3b = $('input[name=cp3b]:checked').val();
    if(cp3b === 'AYES'){cp3b = 1;}
    else{cp3b = 0;}
    console.log('benchScore cp3b=> '+cp3b);

    var cp4b = $('input[name=cp4b]:checked').val();
    if(cp4b === 'AYES'){cp4b = 1;}
    else{cp4b = 0;}
    console.log('benchScore cp4b=> '+cp4b);

    var cp5b = $('input[name=cp5b]:checked').val();
    if(cp5b === 'AYES'){cp5b = 1;}
    else{cp5b = 0;}
    console.log('benchScore cp5b=> '+cp5b);

    var cp6b = $('input[name=cp6b]:checked').val();
    if(cp6b === 'AYES'){cp6b = 1;}
    else{cp6b = 0;}
    console.log('benchScore cp6b=> '+cp6b);

    var cp7b = $('input[name=cp7b]:checked').val();
    if(cp7b === 'AYES'){cp7b = 1;}
    else{cp7b = 0;}
    console.log('benchScore cp7b=> '+cp7b);

    var cp8b = $('input[name=cp8b]:checked').val();
    if(cp8b === 'AYES'){cp8b = 1;}
    else{cp8b = 0;}
    console.log('benchScore cp8b=> '+cp8b);

    var cp9b = $('input[name=cp9b]:checked').val();
    if(cp9b === 'AYES'){cp9b = 1;}
    else{cp9b = 0;}
    console.log('benchScore cp9b=> '+cp9b);

    // var cp10b = $('input[name=cp10b]:checked').val();
    // if(cp10b === 'AYES'){cp10b = 1;}
    // else{cp10b = 0;}
    // console.log('benchScore cp10b=> '+cp10b);

    // var cp11b = $('input[name=cp11b]:checked').val();
    // if(cp11b === 'AYES'){cp11b = 1;}
    // else{cp11b = 0;}
    // console.log('benchScore cp11b=> '+cp11b);

    // var cp12b = $('input[name=cp12b]:checked').val();
    // if(cp12b === 'AYES'){cp12b = 1;}
    // else{cp12b = 0;}
    // console.log('benchScore cp12b=> '+cp12b);

    // var cp13b = $('input[name=cp13b]:checked').val();
    // if(cp13b === 'AYES'){cp13b = 1;}
    // else{cp13b = 0;}
    // console.log('benchScore cp13b=> '+cp13b);

    // var cp14b = $('input[name=cp14b]:checked').val();
    // if(cp14b === 'AYES'){cp14b = 1;}
    // else{cp14b = 0;}
    // console.log('benchScore cp14b=> '+cp14b);

    // var cp15b = $('input[name=cp15b]:checked').val();
    // if(cp15b === 'AYES'){cp15b = 1;}
    // else{cp15b = 0;}
    // console.log('benchScore cp15b=> '+cp15b);

    // var cp16b = $('input[name=cp16b]:checked').val();
    // if(cp16b === 'AYES'){cp16b = 1;}
    // else{cp16b = 0;}
    // console.log('benchScore cp16b=> '+cp16b);

    // var cp17b = $('input[name=cp17b]:checked').val();
    // if(cp17b === 'AYES'){cp17b = 1;}
    // else{cp17b = 0;}
    // console.log('benchScore cp17b=> '+cp17b);
    
    benchmarkScore =  parseFloat(cp1b) + parseFloat(cp2b) + parseFloat(cp3b) + parseFloat(cp4b) + parseFloat(cp5b) + parseFloat(cp6b) + parseFloat(cp7b) + parseFloat(cp8b) + parseFloat(cp9b) // + parseFloat(cp10b) + parseFloat(cp11b) + parseFloat(cp12b) + parseFloat(cp13b) + parseFloat(cp14b) + parseFloat(cp15b) + parseFloat(cp16b) + parseFloat(cp17b);
    healthScore = parseFloat(cp1b)+parseFloat(cp2b)+parseFloat(cp3b)+parseFloat(cp4b)
    stableScore = parseFloat(cp5b)
    safeScore = parseFloat(cp6b)+parseFloat(cp7b)+parseFloat(cp8b)
    schoolScore = parseFloat(cp9b)

    console.log('TOTAL benchScore=> '+benchmarkScore);
    
    var bench_array = [];
    
    bench_array.push( cp1b );
    bench_array.push( cp2b );
    bench_array.push( cp3b );
    bench_array.push( cp4b );
    bench_array.push( cp5b );
    bench_array.push( cp6b );
    bench_array.push( cp7b );
    bench_array.push( cp8b );
    bench_array.push( cp9b );
    // bench_array.push( cp10b );
    // bench_array.push( cp11b );
    // bench_array.push( cp12b );
    // bench_array.push( cp13b );
    // bench_array.push( cp14b );
    // bench_array.push( cp15b );
    // bench_array.push( cp16b );
    // bench_array.push( cp17b );
    $('input[name=cp74q]').val(benchmarkScore); //  Overall number of points

    $('input[name=p75q]').val(healthScore); // Healthy Domain
    $('input[name=p76q]').val(stableScore); // Stable Domain
    $('input[name=p77q]').val(safeScore); // Safe Domain
    $('input[name=p78q]').val(schoolScore); // Schooled Domain
    $('input[name=p79q]').val(healthScore+stableScore+safeScore+schoolScore); //Total Score
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
                    // $('input[name=cp74q]').val(benchmarkScore);
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
            if(thisval == arrayOfExpectedValues[inx]){
                proceed += 1;
                return proceed
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