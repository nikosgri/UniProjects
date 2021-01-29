package commands;

import static org.junit.jupiter.api.Assertions.*;

import java.awt.event.ActionEvent;
import java.io.IOException;

import org.junit.jupiter.api.Test;

class usFour {
	private String file;
	private boolean check;
	private String newS;
	
	@Test
	void test() throws IOException{
		OpenDocument open = new OpenDocument();
		file=open.openFile("C:/Users/Medusa/eclipse-workspace/Software engineering/nikosgri.txt");
		newS=open.give(" title:nikosauthor:grigoriadisdate:Sat May 23 22:45:23 EEST 2020savedate:Sat May 23 22:45:29 EEST 2020--------------------------------------mia grammi");
		check=open.check(newS,file);
		assertEquals(true,check);
	}

}
