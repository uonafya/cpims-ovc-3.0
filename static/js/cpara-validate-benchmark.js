// validBench(['cp3d','cp4d','cp5d','cp6d','if_ovc', 'cp1q', 'cp3q', 'cp4q'], ['AYES','AYES','AYES','AYES','AYES','AYES','AYES','AYES'], 'cp1b');

// cpara v1

// validBench(['if_ovc', 'cp1q', 'cp3q', 'cp4q'], ['AYES','AYES','AYES','AYES'], 'cp1b');
validBench(['cp1q', 'cp3q', 'cp4q'], ['AYES','AYES','AYES'], 'cp1b');
// validBench(['cp5q', 'cp6q', 'cp7q'], ['AYES','AYES','AYES'], 'cp2b');
validBench(['cp7q'], ['AYES'], 'cp2b');
// validBench(['u10_know_status', 'cp8q', 'cp9q', 'cp10q', 'cp11q', 'cp12q', 'o10_know_status', 'cp13q', 'cp14q', 'cp15q', 'cp16q', 'cp17q'], ['AYES','AYES','AYES', 'AYES','AYES','AYES', 'AYES','AYES','AYES', 'AYES','AYES','AYES'], 'cp3b');
validBench(['cp8q', 'cp9q', 'cp10q', 'cp11q', 'cp12q', 'o10_know_status', 'cp13q', 'cp14q', 'cp15q', 'cp16q', 'cp17q'], ['AYES','AYES', 'AYES','AYES','AYES', 'AYES','AYES','AYES', 'AYES','AYES','AYES'], 'cp3b');
// validBench(['adole_preg_hiv', 'cp19q', 'adole_preg_testpos', 'cp20q', 'cp21q', 'adole_wo_deliv','cp22q','cp23q','cp23qa','cp23qb','cp23qc','cp23qd'], ['AYES','AYES','AYES','AYES','AYES','AYES','AYES','AYES','AYES','AYES','AYES','AYES'], 'cp4b');
validBench(['cp19q','cp20q','cp21q','cp22q','cp23q'], ['AYES','AYES','AYES','AYES','AYES'], 'cp4b');
///////////////////////////////////////////////validBench(['cp19q', 'adole_preg_testpos', 'cp20q', 'cp21q', 'adole_wo_deliv','cp22q','cp23q','cp23qa','cp23qb','cp23qc','cp23qd'], ['AYES','AYES','AYES','AYES','AYES','AYES','AYES','AYES','AYES','AYES','AYES'], 'cp4b');
// validBench(['adole_gb_hse', 'cp24q', 'cp25q','cp26q','cp27q','cp28q','cp29q'], ['AYES','AYES','AYES','AYES','AYES','AYES','AYES'], 'cp5b');
validBench(['cp24q', 'cp25q','cp26q','cp27q','cp28q','cp29q'], ['AYES','AYES','AYES','AYES','AYES','AYES'], 'cp5b');
// validBench(['child_w_disab_hse', 'cp30q', 'cp31q'], ['AYES','AYES','AYES'], 'cp6b');
validBench(['cp30q', 'cp31q'], ['AYES','AYES'], 'cp6b');
validBench(['cp32q', 'cp33q', 'cp35q'], ['AYES','AYES','AYES'], 'cp7b');
validBench(['cp36q', 'cp37q', 'cp38q'], ['AYES','AYES','AYES'], 'cp8b');
validBench(['cp39q', 'cp40q'], ['AYES','AYES'], 'cp9b');
validBench(['cp41q', 'cp42q', 'cp43q'], ['AYES','AYES','AYES'], 'cp10b');
// validBench(['child_hd_hse', 'cp44q', 'cp45q','cp46q','cp47q','cp48q'], ['AYES','AYES','AYES','AYES','AYES','AYES'], 'cp11b');
validBench(['cp44q', 'cp45q','cp46q','cp47q','cp48q'], ['AYES','AYES','AYES','AYES','AYES'], 'cp11b');
validBench(['cp49q', 'cp50q', 'cp51q', 'o5y_cd_hse', 'cp52q', 'cp53q', 'cp54q'], ['AYES','AYES','AYES','AYES','AYES','AYES','AYES'], 'cp12b');
// validBench(['cld_rsk_abus', 'cp55q', 'cp56q', 'cp57q', 'cp58q', 'cp59q'], ['AYES','AYES','AYES','AYES','AYES','AYES'], 'cp13b');
validBench(['cp55q', 'cp56q', 'cp57q', 'cp58q', 'cp59q'], ['AYES','AYES','AYES','AYES','AYES'], 'cp13b');
validBench(['cp60q', 'cp61q'], ['AYES','AYES'], 'cp14b');
validBench(['cp62q', 'cp63q','cp64q','cp65q'], ['AYES','AYES','AYES','AYES'], 'cp15b');
validBench(['cp66q', 'cp67q','cp68q','cp69q','cp70q'], ['AYES','AYES','AYES','AYES','AYES'], 'cp16b');
// validBench(['adole_in_vc_train', 'cp71q','cp72q','cp73q'], ['AYES','AYES','AYES','AYES'], 'cp17b');
validBench(['cp71q','cp72q','cp73q'], ['AYES','AYES','AYES'], 'cp17b');


validDate('cp2d','cp1d','AYES','ANNO');
validDate('cp2q','cp1q','ANNO','AYES');
validDate('children_rsk_hiv_assess_date','cp1q','ANNO','AYES');

var benchmarkScore = 0;
$('input[name=cp74q]').attr('readonly', true);

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

// $('input[name=cp10b]').attr('disabled', true);
$('input[name=cp10b]').click(function(){return false;});

// $('input[name=cp11b]').attr('disabled', true);
$('input[name=cp11b]').click(function(){return false;});

// $('input[name=cp12b]').attr('disabled', true);
$('input[name=cp12b]').click(function(){return false;});

// $('input[name=cp13b]').attr('disabled', true);
$('input[name=cp13b]').click(function(){return false;});

// $('input[name=cp14b]').attr('disabled', true);
$('input[name=cp14b]').click(function(){return false;});

// $('input[name=cp15b]').attr('disabled', true);
$('input[name=cp15b]').click(function(){return false;});

// $('input[name=cp16b]').attr('disabled', true);
$('input[name=cp16b]').click(function(){return false;});

// $('input[name=cp17b]').attr('disabled', true);
$('input[name=cp17b]').click(function(){return false;});


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

    var cp10b = $('input[name=cp10b]:checked').val();
    if(cp10b === 'AYES'){cp10b = 1;}
    else{cp10b = 0;}
    console.log('benchScore cp10b=> '+cp10b);

    var cp11b = $('input[name=cp11b]:checked').val();
    if(cp11b === 'AYES'){cp11b = 1;}
    else{cp11b = 0;}
    console.log('benchScore cp11b=> '+cp11b);

    var cp12b = $('input[name=cp12b]:checked').val();
    if(cp12b === 'AYES'){cp12b = 1;}
    else{cp12b = 0;}
    console.log('benchScore cp12b=> '+cp12b);

    var cp13b = $('input[name=cp13b]:checked').val();
    if(cp13b === 'AYES'){cp13b = 1;}
    else{cp13b = 0;}
    console.log('benchScore cp13b=> '+cp13b);

    var cp14b = $('input[name=cp14b]:checked').val();
    if(cp14b === 'AYES'){cp14b = 1;}
    else{cp14b = 0;}
    console.log('benchScore cp14b=> '+cp14b);

    var cp15b = $('input[name=cp15b]:checked').val();
    if(cp15b === 'AYES'){cp15b = 1;}
    else{cp15b = 0;}
    console.log('benchScore cp15b=> '+cp15b);

    var cp16b = $('input[name=cp16b]:checked').val();
    if(cp16b === 'AYES'){cp16b = 1;}
    else{cp16b = 0;}
    console.log('benchScore cp16b=> '+cp16b);

    var cp17b = $('input[name=cp17b]:checked').val();
    if(cp17b === 'AYES'){cp17b = 1;}
    else{cp17b = 0;}
    console.log('benchScore cp17b=> '+cp17b);
    
    benchmarkScore =  parseFloat(cp1b) + parseFloat(cp2b) + parseFloat(cp3b) + parseFloat(cp4b) + parseFloat(cp5b) + parseFloat(cp6b) + parseFloat(cp7b) + parseFloat(cp8b) + parseFloat(cp9b) + parseFloat(cp10b) + parseFloat(cp11b) + parseFloat(cp12b) + parseFloat(cp13b) + parseFloat(cp14b) + parseFloat(cp15b) + parseFloat(cp16b) + parseFloat(cp17b);
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
    bench_array.push( cp10b );
    bench_array.push( cp11b );
    bench_array.push( cp12b );
    bench_array.push( cp13b );
    bench_array.push( cp14b );
    bench_array.push( cp15b );
    bench_array.push( cp16b );
    bench_array.push( cp17b );
    $('input[name=cp74q]').val(benchmarkScore);
    $('input[name=bench_array]').val(JSON.stringify(bench_array));
    console.log('benchmark_score => '+JSON.stringify(bench_array));
    
    
});
// Cpara

markBenchmark('CP23q_b_1', false)

markBenchmark('CP23q_b_2', false)

markBenchmark('CP23q_b_3', false)

// markBenchmark('CP58q', false)

// Benchmark 1
validBench(['CP1q', 'CP2q', 'CP3q', 'CP4q', 'CP5q'], ['AYES','AYES,ANA','AYES,ANA','AYES','AYES,ANA'], 'CP1b');
// Benchmark 2
validBench(['CP6q','CP7q','CP8q','CP9q','CP10q','CP11q','CP12q','CP13q','CP14q'], ['AYES','AYES,ANA','AYES','AYES','AYES,ANA','AYES','AYES','AYES,ANA','AYES'], 'CP2b');

// Healthy Goal 3 >> Benchmark 3
validBench(['CP23q_b_1','CP23q_b_2','CP23q_b_3'],['AYES','AYES','AYES'],'CP3b')
// Healthy Goal 4 >> Benchmark 4
$('input[name=CP41Skip').change(function (e){
if ($('input[name=CP41Skip]:checked').val()==='ANA'){markBenchmark('CP4b',null);}
else{validBench(['CP18q', 'CP19q', 'CP20q', 'CP21q'], ['AYES','AYES,ANA', 'AYES','AYES'], 'CP4b')};
})
// Stable: Goal 5: >> Benchmark 5
validBench(['CP22q','CP23q','CP24q'], ['AYES,ANA','AYES,ANA','AYES'], 'CP5b');
// Safe: Goal 6 >> Benchmark 6
validBench(['CP28q', 'CP29q'],['AYES','AYES'],'CP6b')
// Safe: Benchmark 7:   
validBench(['CP30q','CP31q'],['AYES','AYES'],'CP7b')
// Safe: Goal 8  >> Benchmark 8
validBench(['CP32q'],['AYES'],'CP8b')
// Schooled: Goal 8: Benachmark 9
validBench(['CP33q','CP34q','CP35q','CP36q'],['AYES','AYES','AYES','AYES'],'CP9b')
// control
validBench(['CP330q','CP340q','CP350q','CP360q'],['AYES','AYES','AYES','AYES'],'CP90b')


validDate('CP2d','CP1d','AYES','ANNO');







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
    if(CP9b === 'AYES'){CP9b = 1;}
    else{CP9b = 0;}
    console.log('benchScore CP9b=> '+CP9b);

    var CP90b = $('input[name=CP90b]:checked').val(); 
    if(CP90b === 'AYES'){CP90b = 0;}
    else{CP90b = 1;}
    console.log('benchScore CP90b=> '+CP90b);
    
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
        console.log('marked bench as passed')
        // $('input[name="'+benchmarkId+'"][value="AYES"]').attr('checked', true);
        $('input[name='+benchmarkId+']').removeAttr('disabled');
        $('input[name='+benchmarkId+'][value=AYES]').prop("checked", true);
        $('input[name='+benchmarkId+']').attr('disabled', true);
    }else if (passOrFail===false){
        console.log('marked bench as failed')
        $('input[name='+benchmarkId+']').removeAttr('disabled');
        $('input[name='+benchmarkId+'][value=ANNO]').prop("checked", true);
        $('input[name='+benchmarkId+']').attr('disabled', true);
    }else{
        console.log('marked bench as null')
        $('input[name='+benchmarkId+']').removeAttr('disabled');
        $('input[name='+benchmarkId+'][value=ANA]').prop("checked", true);
        $('input[name='+benchmarkId+']').attr('disabled', true);
    }
}
// validDate('CP2d','CP1d','AYES','ANNO');
function validDate(dateFieldName, radioToCheck, rightValue, wrongValue) {
    // $('input[name='+dateFieldName+']').attr('disabled', true);
    $('input[name='+radioToCheck+']').change(function(){
        var valu = $(this).val();
        if(valu === rightValue){
            $('input[name='+dateFieldName+']').datepicker().val('');
            $('input[name='+dateFieldName+']').attr('readonly', true);
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