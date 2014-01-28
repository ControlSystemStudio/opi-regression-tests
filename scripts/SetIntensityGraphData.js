importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var simuData = DataUtil.createDoubleArray(65536);

	for(var i=0; i<256; i++){
		for(var j=0; j<256; j++){
			var x = j-128;
			var y = i-128;		
			var p = Math.sqrt(x*x + y*y);
			simuData[i*256 + j] = Math.sin(p*2*Math.PI/256 + 2);		
		}
	}
widget.setValue(simuData);
	

