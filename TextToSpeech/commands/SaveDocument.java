package commands;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;


import javax.swing.JButton;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextArea;

import com.sun.speech.freetts.Voice;



public class SaveDocument implements ActionListener {
	private JPanel panel;
	private String textArea;
	private JTextArea textAreaSave;
	private JButton speech,LineToSpeech,ReversedSpeech,ReversedLine,Encoding;
	private String fileName;
	private Voice talk;
	
	
	

	@SuppressWarnings("deprecation")
	public SaveDocument(JPanel panel,String textArea,String fileName,Voice talk) {
		this.panel = panel;
		this.textArea = textArea;
		this.fileName = fileName;
		this.talk = talk;
		
		
		
		textAreaSave = new JTextArea(textArea);
		textAreaSave.setBounds(10, 11, 300, 200);
		panel.add(textAreaSave);
		textAreaSave.enable(false);
		
		speech = new JButton("speech");
		speech.setBounds(320, 10, 110, 22);
		panel.add(speech);
		
		ReversedSpeech = new JButton("ReversedSpeech");
		ReversedSpeech.setBounds(320, 40, 110, 22);
		panel.add(ReversedSpeech);
		
		LineToSpeech = new JButton("LineToSpeech");
		LineToSpeech.setBounds(320, 70, 110, 22);
		panel.add(LineToSpeech);
		
		ReversedLine = new JButton("ReversedLine");
		ReversedLine.setBounds(320, 100, 110, 22);
		panel.add(ReversedLine);
		
		Encoding = new JButton("Encoding");
		Encoding.setBounds(320, 130, 110, 22);
		panel.add(Encoding);
		
		//elenxoume poia class kalese thn saveDocument(dhladh h NewDocument h openDocument)
		//kai analoga zhtaei h den zhtaei apo ton xrhsth.
		if(fileName ==null) {
			
			this.fileName = JOptionPane.showInputDialog(null,"enter filename:");
			
			try {
				PrintWriter file = new PrintWriter(this.fileName+".txt");
				file.println(textArea);
				file.close();
			} catch (FileNotFoundException e1) {
				e1.printStackTrace();
			}
		}

		
		
		speech.addActionListener(this);
		LineToSpeech.addActionListener(this);
		ReversedSpeech.addActionListener(this);
		ReversedLine.addActionListener(this);
		Encoding.addActionListener(this);
		
		
	}
	
	public void actionPerformed(ActionEvent e) {
		
		
		if(e.getSource()==speech) {
			try {
				//System.out.println(talk.getVolume());
				//System.out.println(talk.getRate());
				//System.out.println(talk.getPitch());
				
				
				
				//////////////////////
				//anoigoume to arxeio kai afou paralhpsoume ths 5 prwtes grammes , vazoume to programma na diavasei tis upoloipes
				FileReader reader = new FileReader(fileName+".txt");
				BufferedReader br = new BufferedReader(reader);
				String line;
				int counter = 0;
				
				line = br.readLine();
				while(line!=null) {
					if(counter>4) {
						talk.allocate();
						talk.speak(line);
						line = br.readLine();
						counter++;
					}else {
						line = br.readLine();
						counter++;
					}
				}
				br.close();
				reader.close();
			} catch (FileNotFoundException e1) {
				e1.printStackTrace();
			} catch (IOException e1) {
				e1.printStackTrace();
			}	
		}
		//diavazoume xekinontas apo thn teleutaia lexh tis teleutaias grammhs kai sunexizoume pros ta panw apouhkeuontas ta se ena voh8htiko string kai pali paraloipoume tis 5 prwtes grammes
		else if(e.getSource()==ReversedSpeech) {
				
				int lineLength = 0;
				String [] textFile = textArea.split("\n");
				for(@SuppressWarnings("unused") String war : textFile) {
					lineLength++;
				}
				
				String reversed = "";
				for(int i = lineLength-1;i>=5;i--) {
					
					String [] Line = textFile[i].split(" ");
					int wordLength = 0;
					String reversedLine = "";
					for(@SuppressWarnings("unused") String war : Line) {
						wordLength++;
					}
					for(int j = wordLength-1;j>=0;j--) {
						reversedLine = reversedLine + Line[j] + " ";
					}
					reversed = reversed + reversedLine+"\n";
					
				}
				
				talk.allocate();
				talk.speak(reversed);
			
		}
		else if(e.getSource()==LineToSpeech) {
			CommandsFactory a = new CommandsFactory();
			//katastrefoume to panel ,wste sthn epomenh class pou 8a to steiloume  na to lavei adeio kai na kanei oti 8elei mesa.
			panel.removeAll();
			panel.repaint();
			//kaloume tis set me8odous tis factory wste h class pou 8a kalesoume meta na exei parei ta swsta orismata
			a.setPanel(panel);
			a.setFileName(fileName);
			a.setTalk(talk);
			a.setFlag(0);
			a.createCommand("LineDoc");
		}
		else if(e.getSource()==ReversedLine) {
			CommandsFactory a = new CommandsFactory();
			//katastrefoume to panel ,wste sthn epomenh class pou 8a to steiloume  na to lavei adeio kai na kanei oti 8elei mesa.
			panel.removeAll();
			panel.repaint();
			//kaloume tis set me8odous tis factory wste h class pou 8a kalesoume meta na exei parei ta swsta orismata
			a.setPanel(panel);
			a.setFileName(fileName);
			a.setTalk(talk);
			a.setFlag(1);
			a.createCommand("LineDoc");
		}
		else if(e.getSource()==Encoding) {
			CommandsFactory a = new CommandsFactory();
			//katastrefoume to panel ,wste sthn epomenh class pou 8a to steiloume  na to lavei adeio kai na kanei oti 8elei mesa.
			panel.removeAll();
			panel.repaint();
			//kaloume tis set me8odous tis factory wste h class pou 8a kalesoume meta na exei parei ta swsta orismata
			a.setPanel(panel);
			a.setTextArea(textArea);
			a.setTalk(talk);
			a.setFileName(fileName);
			a.createCommand("encodingDoc");
			
		}
		
		
		
	}
	

	


}
