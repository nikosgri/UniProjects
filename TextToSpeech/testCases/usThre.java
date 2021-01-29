package commands;

import static org.junit.jupiter.api.Assertions.*;

import java.io.IOException;

import org.junit.jupiter.api.Test;

class usThre {
	private String file;
	private String s;
	private boolean check;
	@Test
	void test() throws IOException {
		EditDocument e = new EditDocument();
		file=e.openFile();
		s=e.beforeSave("title:nikosauthor:grigoriadisdate:Sat May 23 22:45:23 EEST 2020savedate:Sat May 23 22:45:29 EEST 2020--------------------------------------mia grammi");
		check=e.checkFiles(s, file);
		assertEquals(true,check);
	}

}
