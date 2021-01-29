package commands;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import javax.swing.JButton;
import javax.swing.JFileChooser;
import javax.swing.JPanel;
import javax.swing.JTextArea;

import com.sun.speech.freetts.Voice;

public class OpenDocument implements ActionListener {
	
	private JPanel panel;
	private JFileChooser fileOpen = new JFileChooser();
	private JButton saveButtonOpen;
	private java.io.File file;
	private JTextArea textAreaOpen;
	private Voice talk;
	public String l = " ";
	
	public OpenDocument() {
		
	}
	
	
	public OpenDocument(JPanel panel,Voice talk) {
		this.panel = panel;
		this.talk = talk;
		panel.removeAll();
		panel.repaint();
		
		textAreaOpen = new JTextArea();
		textAreaOpen.setBounds(10, 11, 300, 200);
		panel.add(textAreaOpen);
		
		saveButtonOpen = new JButton("save");
		saveButtonOpen.setBounds(320, 100, 110, 22);
		panel.add(saveButtonOpen);
		
		//zhtame apo ton xrhsth na epilexei pio programma 8elei na anoixei.
		if(fileOpen.showOpenDialog(null) == JFileChooser.APPROVE_OPTION) {
			file = fileOpen.getSelectedFile();
			try {
				FileReader reader = new FileReader(file);
				BufferedReader br = new BufferedReader(reader);
				textAreaOpen.read(br, null);
				br.close();
				textAreaOpen.requestFocus();
			} catch (IOException e1) {
				e1.printStackTrace();
			}
    	}		
		
		
		
		saveButtonOpen.addActionListener(this);
		
		
	}
	
	 public void actionPerformed(ActionEvent e) {
		 if(e.getSource() == saveButtonOpen) {
			
			CommandsFactory a = new CommandsFactory();
			String textArea = textAreaOpen.getText();
			a.setPanel(panel);
			a.setTextArea(textArea);
			a.setTalk(talk);
			panel.removeAll();
			panel.repaint();
			a.createCommand("saveDoc");
		 }
	   
		 
	 }
	 ////////////for the tests
	 public String beforeOpen(String x) {
	    	return x;
	 }
	 public String  openFilename()  {
	   try {
		//vazoume to file path tou arxeiou pou 8eloume na doume an anoigei
		   
	    FileReader file = new FileReader("C:/Users/giorgos/eclipse-workspace/texnologiaLogismikou/alex.txt"); /*na to allaksw*/

		@SuppressWarnings("resource")
		BufferedReader read = new BufferedReader(file);
	          String line = read.readLine();
	          while(line!=null) {
	          l+=line;
	          line=read.readLine();
	          }
	        	
	    }catch(Exception e) {
	    		
	    	System.out.println("sdf");
	    }
	    return l;
	}
	public boolean checkOpen(String r,String y) {
	    if(r.equals(y)) {
	    	return true;
	    }else {
	    	return false;
	    }
	}
	/////////////////////////


}
