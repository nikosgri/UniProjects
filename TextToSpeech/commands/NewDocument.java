package commands;


import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Date;
import javax.swing.JButton;

import javax.swing.JLabel;

import javax.swing.JPanel;
import javax.swing.JTextArea;
import javax.swing.JTextField;

import com.sun.speech.freetts.Voice;



public class NewDocument implements ActionListener{
	
    private JTextField titleField,authorField;
    private String title,author;
    private Date date;
    private JButton editButton;
    private JPanel panel;
    private Voice talk;
    private String date2;
    private String all;

    //for the tests
    public NewDocument(String a , String b,String t) {
    	this.title=a;
    	this.author=b;
    	this.date2=t;
    }
    public String getS(String a , String b,String t) {
		this.title=a;
		this.author=b;
		this.date2=t;
		all = this.title+"\n" + this.author+"\n" +this.date2;
		return all;
    }
    ///
    
    //ftiaxnoume to panel mas opws 8eloume kai vazoume kai ena button to opoio an pathsoume mpainoume mesa sth actionPerformed
    public NewDocument(JPanel panel,Voice talk) {
    	this.panel = panel;
    	this.talk = talk;
    	
    	panel.removeAll();
		panel.repaint();
		
    	JLabel titleLabel = new JLabel("title:");
		titleLabel.setBounds(39, 54, 46, 14);
		panel.add(titleLabel);
		
		JLabel authorLabel = new JLabel("author:");
		authorLabel.setBounds(39, 138, 46, 14);
		panel.add(authorLabel);
		
		titleField = new JTextField();
		titleField.setBounds(134, 51, 86, 20);
		panel.add(titleField);
		titleField.setColumns(10);
		
		authorField = new JTextField();
		authorField.setBounds(134, 135, 86, 20);
		panel.add(authorField);
		authorField.setColumns(10);
		
		editButton = new JButton("edit");
		editButton.setBounds(320, 100, 110, 22);
		panel.add(editButton);
		
		editButton.addActionListener(this);

    }
    public void actionPerformed(ActionEvent e) {
    	if(e.getSource() == editButton) {
    		date = new Date();
    		title = titleField.getText();
    		author = authorField.getText();
    		//eisagoume to title ,to author kai to creation date mesa se ena string
    		JTextArea helpArea = new JTextArea("title:"+title+"\n"+
					"author:"+author+"\n"+
					"date:"+date);
    		CommandsFactory a = new CommandsFactory();
    		//kaloume tis set me8odous tis factory wste h class pou 8a kalesoume meta na exei parei ta swsta orismata
    		a.setPanel(panel);
    		a.setTextArea(helpArea.getText());
    		a.setTalk(talk);
    		//katastrefoume to panel ,wste sthn epomenh class pou 8a to steiloume  na to lavei adeio kai na kanei oti 8elei mesa.
    		panel.removeAll();
            panel.repaint();
    		a.createCommand("editDoc");
    	}
    }
    //for the tests
    public  int countLines(String str){
  	   String[] lines = str.split("\r\n|\r|\n");
  	   return  lines.length;
  	   
    }
    
    
     public boolean isEmpty(String x) {
     	if(countLines(x)==3) {
     		return true;
     	}else {
     		return false;
     	}
     }
     ////////////
}

