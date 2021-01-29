package commands;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class usOne {

	private boolean check;
	private String x;
	@Test
	void test() {
		NewDocument m = new NewDocument("nikos","grigoriadis","date:Sat May 23 22:45:23 EEST 2020");
		String value = m.getS("nikos","grigoriadis","date:Sat May 23 22:45:23 EEST 2020"); 
		x=value;
		check = m.isEmpty(x);
		assertEquals(true,check);
		
	}

}
