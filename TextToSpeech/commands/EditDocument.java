package commands;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Date;


import javax.swing.JButton;

import javax.swing.JPanel;
import javax.swing.JTextArea;

import com.sun.speech.freetts.Voice;

public class EditDocument implements ActionListener {
	
   
    private String TiAuDaArea;
    private JTextArea textAreaEdit;
    private JPanel panel;
    private JButton saveButton;
    private Date savedate;
    private Voice talk;
    private String addArea,addAreaNew,str;
    private String k="";

    //for the tests
	public EditDocument() {
    	
    }

    
    public EditDocument(String addArea,String addAreaNew,String str) {
    	this.addArea = addArea;
    	this.addAreaNew = addAreaNew;
    	this.str = str;
    			
    	
    }
    ////
    
   


    
    
    
    public EditDocument(JPanel panel,String TiAuDaArea,Voice talk) {
    	this.panel = panel;
    	this.TiAuDaArea = TiAuDaArea;
    	this.talk = talk;
    	
    	textAreaEdit = new JTextArea();
    	textAreaEdit.setBounds(10, 11, 300, 200);
		panel.add(textAreaEdit);
		
		saveButton = new JButton("save");
		saveButton.setBounds(320, 100, 110, 22);
		panel.add(saveButton);
		
		
		saveButton.addActionListener(this);
        

    }
    public void actionPerformed(ActionEvent e) {
    	if(e.getSource() == saveButton) {
    		savedate = new Date();
    		//vazoume mesa se ena neo string to string pou lavame apo thn newDocument kai epipleon vazoume to saveDate kai auta pou grapsame mesa sto textArrea.
    		JTextArea helpArea = new JTextArea(TiAuDaArea+"\n"+
    											"savedate:"+savedate+"\n"+
    											"--------------------------------------"+"\n"+
    											textAreaEdit.getText());
    		CommandsFactory a = new CommandsFactory();
    		String textArea = helpArea.getText();
    		//kaloume tis set me8odous tis factory wste h class pou 8a kalesoume meta na exei parei ta swsta orosmata
    		a.setPanel(panel);
    		a.setTextArea(textArea);
    		a.setTalk(talk);
    		//katastrefoume to panel ,wste sthn epomenh class pou 8a to steiloume  na to lavei adeio kai na kanei oti 8elei mesa.
    		panel.removeAll();
    		panel.repaint();
    		
		
    		a.createCommand("saveDoc");
    	}
    	
        
    }
    //for the tests  
    public String addArea(String s,String h) {
		String all;
		all = s + h;
		
		return all;
		
	}
	public boolean isTrue(String t,String newS) {

        if(t.equals(newS)) {
            return false;
        }else {
            return true;
        }
    }
	 public String beforeSave(String x) {
	    	return x;
	    }
	    public String  openFile()  {
	    	try {
	    		//8etoume to filePath pou 8eloume na elenxoume!!!!!!!
	    		FileReader file = new FileReader("C:/Users/giorgos/eclipse-workspace/texnologiaLogismikou/alex.txt"); /*na to allaksw*/
	        	BufferedReader read = new BufferedReader(file);
	            String line = read.readLine();
	            while(line!=null) {
	            	k+=line;
	            	line=read.readLine();
	            }
	        	
	    	}catch(Exception e) {
	    		System.out.println("sdf");
	    	}
	    	return k;
	    }
	    public boolean checkFiles(String r,String y) {
	    	if(r.equals(y)) {
	    		return true;
	    	}else {
	    		return false;
	    	}
	    }
	   ////////////////////

}