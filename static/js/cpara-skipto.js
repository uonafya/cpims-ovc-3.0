// cpara 
triggerSkip('CP31Skip','ANA','CP41Skip','2')

triggerSkip('CP2bSkip','ANA','CP2b','2')

triggerSkip('CP27Skip','ANA','CP2b','2')

triggerSkip('CP6Skip','ANA','CP6b','4');
// triggerSkip('CP63Skip','ANA','CP58q','4');


triggerSkip('CP93Skip','ANA','CP35q','5');
triggerSkip('CP91Skip','ANA','CP9b','5');

triggerSkip('CP41Skip','ANA','CP4b','2');
triggerSkip('CP44Skip','ANA','CP21q','2');

// Hard coded
// Skip 2.1
$('input[name=CP21Skip]').change(function(){
    // console.log('Hello')
    let this_value = $('input[name=CP21Skip]:checked').val()
    
    
    if(this_value==='AYES'){
        $('input[name=CP6q],input[name=CP7q],input[name=CP8q]').prop('readonly', false)
        $('input[name=CP6q],input[name=CP7q],input[name=CP8q]').prop('checked', false);
        $('input[name=CP6q],input[name=CP7q],input[name=CP8q]').unbind('click')
        $('.skip21').removeClass('hidden').after('')
        $('.skyp1').remove();
        

    }else{
        $('input[name=CP6q][value=AYES],input[name=CP7q][value=AYES],input[name=CP8q][value=AYES]').prop('checked', true);
        $('input[name=CP6q],input[name=CP7q],input[name=CP8q]').prop('required', false)
        $('input[name=CP6q],input[name=CP7q],input[name=CP8q]').click(function(){return false;});
        $('.skip21').addClass('hidden').after('<span class="skyp1"><br><i style="color: grey;">Skipped questions</i><br/></span>')
    }
})

// Skip 2.1
$('input[name=CP24Skip]').change(function(){
    // console.log('Hello')
    let this_value = $('input[name=CP24Skip]:checked').val()
    
    if(this_value==='AYES'){
        $('input[name=CP9q],input[name=CP10q],input[name=CP11q]').prop('readonly', false);
        $('input[name=CP9q],input[name=CP10q],input[name=CP11q]').prop('checked', false);
        $('input[name=CP9q],input[name=CP10q],input[name=CP11q]').unbind('click');
        $('.skip24').removeClass('hidden').after('');
        $('.skyp2').remove();

    }else{
        $('input[name=CP9q][value=AYES],input[name=CP10q][value=AYES],input[name=CP11q][value=AYES]').prop('checked', true);
        $('input[name=CP9q],input[name=CP10q],input[name=CP11q]').prop('required', false)
        $('input[name=CP9q],input[name=CP10q],input[name=CP11q]').click(function(){return false;});
        $('.skip24').addClass('hidden').after('<span class="skyp2"><br><i style="color: grey;">Skipped questions</i><br/></span>')
    }
})
// triggerSkip('CP21Skip','ANA','CP27q','2')

// Skip 6.3
$('input[name=CP63Skip]').change(function(){
    // console.log('Hello')
    let this_value = $('input[name=CP63Skip]:checked').val()
    
    if(this_value==='AYES'){       
        $('input[name=CP58q]').prop('checked', false)
        $('input[name=CP58q]').attr('disabled', false)
        $('.r13q1').removeClass('hidden').after('');
        $('.skyp3').remove();

    }else{
        $('input[name=CP58q][value=AYES]').prop('checked', true)
        $('input[name=CP58q]').attr('disabled', true)
        // &("input[name*='CP27q']").prop('checked', true)
        $('.r13q1').addClass('hidden').after('<span class="skyp3"><br><i style="color: grey;">Skipped questions</i><br/></span>')
    }
})




// Cpara v1

// QuestionSkipLogic
//format is:   triggerSkip(inputToCheck,rightValue,questionToGoTo,tabContainingDestinationQn);
    // Q1 -> Q2
    triggerSkip('if_ovc','ANNO','cp5q','2');
    triggerSkip('u10_know_status','ANNO','o10_know_status','2');
    triggerSkip('o10_know_status','ANNO','adole_preg_hiv','2');
    triggerSkip('adole_preg_hiv','ANNO','cp24q','2');
    triggerSkip('adole_preg_testpos','ANNO','cp24q','2');
    triggerSkip('adole_wo_deliv','ANNO','cp24q','2');
    triggerSkip('cp23q','ANNO','cp24q','2');
    triggerSkip('adole_gb_hse','ANNO','cp30q','2');
    triggerSkip('child_w_disab_hse','ANNO','cp32q','3');
    //<TODOne just test
    // triggerSkip('cp5d','ANNO','cp32q','1');
    // triggerSkip('cp3d','ANNO','cp49q','1');
    triggerSkip('adole_gb_hse2','ANNO','cp30q','2');
    //>TODOne just test
    triggerSkip('child_abv_10y','ANNO','cp36q','3');
    triggerSkip('u_chd_sck','ANNO','cp43q','3');
    triggerSkip('chd_ovr_10','ANNO','child_hd_hse','4');
    triggerSkip('chd_ovr_10y','ANNO','cp49q','4');
    triggerSkip('child_hd_hse','ANNO','cp49q','4');
    triggerSkip('o5y_cd_hse','ANNO','cp55q','4');
    triggerSkip('o10y_cd_hse','ANNO','cp60q','4');
    triggerSkip('cld_rsk_abus','ANNO','cp60q','4');
    triggerSkip('chd_ovr_10ys','ANNO','cp62q','4');
    triggerSkip('adole_in_vc_train','ANNO','cp74q','5');
    
    // triggerSkip('cp49q','AYES','q12p4','4');
    triggerSkip('cp49q','AYES','o5y_cd_hse','4');
    triggerSkip('cp50q','ANNO','q12p4','4');
    triggerSkip('child_bwn_4t5y_Qn','ANNO','cp70q','5');
    triggerSkip('clw_hiv_o5','ANNO','cp8q','2');
    triggerSkip('cp23qa','ANNO','cp24q','2'); 
    triggerSkip('cp23qb','ANNO','cp24q','2'); 
    triggerSkip('cp23qc','ANNO','cp24q','2'); 
    triggerSkip('cp23qd','ANNO','cp24q','2');
    triggerSkip('child_bwn_6t17y_Qn','ANNO','cp69q','5');
// endQuestionSkipLogic





// ------------------------CORE-------------------------
function triggerSkip(inputToCheck,rightValue,toQnID,toTabID) {
    // $('input[name="'+inputToCheck+'"][value="'+rightValue+'"]').on('change', function () {
    $('input[name="'+inputToCheck+'"]').on('change', function () {
        // console.log('onchanging,,,');
        
        var theval = $('input[name="'+inputToCheck+'"]').val();
        // textbox, numbers, dates etc
        if($('input[name="'+inputToCheck+'"]').attr('type') == 'date' || $('input[name="'+inputToCheck+'"]').attr('type') == 'text' || $('input[name="'+inputToCheck+'"]').attr('type') == 'number'){
            var valFromInput = $('input[name="'+inputToCheck+'"]').val();
            if(valFromInput == rightValue){
                var unDo = false
                skipToQn(inputToCheck,toQnID,toTabID,unDo);
            }else{
                var unDo = true;
                skipToQn(inputToCheck,toQnID,toTabID,unDo);
            }
        }
        // END textbox, numbers, dates etc

        // cater for checkbox
        if($('input[name="'+inputToCheck+'"]').attr('type') == 'checkbox'){
            // console.log("checkbox with Name: "+inputToCheck+" found");
            var valFromInput = '';
            $.each($(this), function (chind, eachbx) {
                if($(this).is(':checked')){
                    // console.log("TICKED checkbox with Name: "+inputToCheck+" found");
                    var unDo = false;
                    skipToQn(inputToCheck,toQnID,toTabID,unDo);
                }else{
                    // console.log("UNDO ticked checkbox with Name: "+inputToCheck);
                    var unDo = true;
                    skipToQn(inputToCheck,toQnID,toTabID,unDo);
                }
            });
        }
        // END cater for checkbox

        // cater for radio
        if($('input[name="'+inputToCheck+'"]').attr('type') == 'radio'){
            var valFromInput = $('input[name="'+inputToCheck+'"]:checked').val();
            // console.log("radio with Name: "+inputToCheck+" found");
            // console.log("valFromInput======> "+valFromInput);
            if(valFromInput === rightValue){
                // console.log("TICKED radio with Name: "+inputToCheck+" found. rightValue="+rightValue+" & valFromInput="+valFromInput);
                // console.log("valFromInput: "+valFromInput+" & rightValue: "+rightValue);
                var unDo = false;
                skipToQn(inputToCheck,toQnID,toTabID,unDo);
            }else if(valFromInput !== rightValue){
                // console.log("undoing... ");
                var unDo = true;
                skipToQn(inputToCheck,toQnID,toTabID,unDo);
            }
        }
        //END cater for radio
    });
}
function skipToQn(inputToCheck,toQnID,toTabID,unDo) {
    //hideQnsBtwn
    var destinationT = $('input[name="'+toQnID+'"]').closest("tr");
    if(!unDo){
            $('a[href="#step'+toTabID+'"]').trigger("click");
            $("td").attr("tabindex", "-1");
            $(".form-group").attr("tabindex", "-1");
            $('input[name="'+toQnID+'"]').closest("td").attr("tabindex", "1");
            $('input[name="'+toQnID+'"]').closest(".form-group").attr("tabindex", "1");
            $('input[name="'+toQnID+'"]').closest("td").focus();
            $('input[name='+toQnID+']').removeAttr('required');
			$('input[name='+toQnID+']').attr('data-parsley-required', false);
            $('input[name="'+toQnID+'"]').closest(".form-group").focus();
            // $('input[name="'+inputToCheck+'"]').closest(".form-group").nextUntil(destinationT, "tr").addClass('hidden');
            
            $('input[name="'+inputToCheck+'"]').closest(".col-md-12").nextUntil(destinationT, ".col-md-12").find('input').attr('data-parsley-required', false).removeAttr('required');
            
            //tick AYES for skipped qns
            $('input[name="'+inputToCheck+'"]').closest(".col-md-12").nextUntil(destinationT, ".col-md-12").find('input[value=AYES]').prop("checked", true);
            $('input[name="'+inputToCheck+'"]').closest(".col-md-12").nextUntil(destinationT, ".col-md-12").find('tr').not(':last-of-type').find('td').not(':first-of-type').css('background', '#dddddd');
            $('input[name="'+inputToCheck+'"]').closest(".col-md-12").nextUntil(destinationT, ".col-md-12").find('td input[type=radio]').attr('disabled', 'disabled').attr('data-parsley-required', false).removeAttr('required');
            //tick AYES for skipped qns

            $('input[name="'+inputToCheck+'"]').closest(".col-md-12:not(.containsTable)").nextUntil(destinationT, ".col-md-12:not(.containsTable)").find('.form-group').not('.note-info').addClass('hidden').after('<span id="skyp"><br><i style="color: grey;">Skipped question</i><br/></span>');
            
            //tick Benchmark
            $('input[name="'+inputToCheck+'"]').closest(".col-md-12").nextUntil(destinationT, ".col-md-12").find('.note-info').find('input[value=AYES]').prop('checked', true).trigger('click').css('color', 'green');
            $('input[name="'+inputToCheck+'"]').closest(".col-md-12").nextUntil(destinationT, ".col-md-12").find('.form-group.note-info input[value="AYES"]').prop('checked',true);
            //tick Benchmark

            $('input[name="'+toQnID+'"]').closest("td").css('outline', '3px solid #32a1ce');
            $('input[name="'+toQnID+'"]').closest(".form-group").css('outline', '3px solid #32a1ce');
            console.log("skipping to Qn: "+toQnID+" on Tab: "+toTabID);
        }
        if(unDo){
            // console.log("undoing2... ");
            $("td").attr("tabindex", "-1");
            $(".form-group").attr("tabindex", "-1");
            $('input[name="'+inputToCheck+'"]').closest("td").attr("tabindex", "1");
            $('input[name="'+inputToCheck+'"]').closest(".form-group").attr("tabindex", "1");
            $('input[name="'+inputToCheck+'"]').closest("td").focus();
            $('input[name="'+inputToCheck+'"]').closest(".form-group").focus();
            $('input[name="'+inputToCheck+'"]').closest("tr").nextUntil(destinationT, "tr").removeClass('hidden');

            $('input[name="'+inputToCheck+'"]').closest(".col-md-12").nextUntil(destinationT, ".col-md-12").find('.form-group').removeClass('hidden').after('');
            //UNtick AYES for skipped qns
            $('input[name="'+inputToCheck+'"]').closest(".col-md-12").nextUntil(destinationT, ".col-md-12").find('input[value=AYES]').prop("checked", false);
            $('input[name="'+inputToCheck+'"]').closest(".col-md-12").nextUntil(destinationT, ".col-md-12").find('tr').not(':last-of-type').find('td').not(':first-of-type').css('background', '##ffffff');
            $('input[name="'+inputToCheck+'"]').closest(".col-md-12").nextUntil(destinationT, ".col-md-12").find('td input[type=radio]').removeAttr('disabled');
            //UNtick AYES for skipped qns
            //benchmark=no for skipped qns
            $('input[name="'+inputToCheck+'"]').closest(".col-md-12").nextUntil(destinationT, ".col-md-12").find('.form-group.note-info input[value="ANNO"]').prop('checked',true);
            //benchmark=no for skipped qns

            $('input[name="'+inputToCheck+'"]').closest(".col-md-12").nextUntil(destinationT, ".col-md-12").find('#skyp').remove();

            // $('input[name="'+inputToCheck+'"]').closest(".col-md-12").nextUntil(destinationT, ".form-group").find('input').attr('required');
            
            $('input[name="'+inputToCheck+'"]').closest("td").css('outline', '1px solid #32a1ce');
            $('input[name="'+inputToCheck+'"]').closest(".form-group").css('outline', '1px solid #32a1ce');
            
            $('input[name="'+destinationT+'"]').closest("td").css('outline', 'none');
            $('input[name="'+destinationT+'"]').closest(".form-group").css('outline', 'none');
            console.log("UNDO skipping to Qn: "+toQnID+" on Tab: "+toTabID);
        }
    //hideQnsBtwn
}
// ------------------------endCORE-------------------------
