package commands;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextArea;
import javax.swing.JTextField;

import com.sun.speech.freetts.Voice;

public class LineToSpeech implements ActionListener {
	private JPanel panel;
	private String fileName;
	private JTextArea textArea;
	private JTextField lineField;
	private JButton enterButton,backButton;
	private int flag;
	private Voice talk;
	
	
	@SuppressWarnings("deprecation")
	public LineToSpeech(JPanel panel,String fileName,int flag,Voice talk){
		this.panel = panel;
		this.fileName = fileName;
		this.flag = flag;
		this.talk = talk;
		
		
		
		textArea = new JTextArea();
		textArea.setBounds(10, 11, 300, 200);
		panel.add(textArea);
		
		JLabel lblNewLabel = new JLabel("Line:");
		lblNewLabel.setBounds(360, 74, 46, 14);
		panel.add(lblNewLabel);
		
		lineField = new JTextField();
		lineField.setBounds(338, 99, 86, 20);
		panel.add(lineField);
		lineField.setColumns(10);
		
		enterButton = new JButton("enter");
		enterButton.setBounds(335, 162, 89, 23);
		panel.add(enterButton);
		
		backButton = new JButton("back");
		backButton.setBounds(335, 40, 89, 23);
		panel.add(backButton);
		
		try {
			FileReader reader = new FileReader(fileName+".txt");
			BufferedReader br = new BufferedReader(reader);
			textArea.read(br, null);
			textArea.enable(false);
			br.close();
			textArea.requestFocus();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		
		
		
		
		
		enterButton.addActionListener(this);
		backButton.addActionListener(this);
		
	
	}
	
	public void actionPerformed(ActionEvent e) {
		if(e.getSource()==enterButton) {
			try {
				FileReader reader = new FileReader(fileName+".txt");
				BufferedReader br = new BufferedReader(reader);
				String line;
				int counter = 0;
				//VoiceManager vs = VoiceManager.getInstance();
				//Voice talk = vs.getVoice("kevin16");
				
				
				
				//an to flag einai 0 tote vazoume to programma na diavasei thn grammh opws einai.
				if(flag == 0) {
					line = br.readLine();
					while(line!=null) {
						if(counter==parsInt(lineField.getText())) {
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
				}
				//an to flag einai 1 tote vazoume to programma na diavasei thn grammh antistrofa.
				else if(flag ==1) {//reverseLine
					line = br.readLine();
					while(line!=null) {
						if(counter==parsInt(lineField.getText())) {
							
							int word = 0;
							String [] words = line.split(" ");
							for(@SuppressWarnings("unused") String war : words) {
								word++;
							}
							String reversed = "";
							for(int i = word-1;i>=0;i--) {
								
								reversed = reversed + words[i]+" ";
							}
							
							talk.allocate();
							talk.speak(reversed);
							line = br.readLine();
							counter++;
						}else {
							line = br.readLine();
							counter++;
						}
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
		//
		else if(e.getSource()==backButton) {
			CommandsFactory a = new CommandsFactory();
			panel.removeAll();
			panel.repaint();
			a.setPanel(panel);
			a.setTextArea(textArea.getText());
			a.setTalk(talk);
			a.setFileName(fileName);
			a.createCommand("saveDoc");
		}
	}
	private int parsInt(String speechline) {
		int i = Integer.parseInt(speechline);
		return i-1;
	}

}
