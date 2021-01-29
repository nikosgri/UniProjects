package commands;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextArea;

import com.sun.speech.freetts.Voice;


public class TuneEncoding implements ActionListener {
	
	private JPanel panel;
	private String textArea,fileName;
	private JTextArea textArea1;
	private JComboBox<String> comboBox;
	private JButton speechButton,backButton,lineEncodeSpeech;
	private Voice talk;
	
	
	public TuneEncoding () {
		
	}
	@SuppressWarnings("deprecation")
	public TuneEncoding (JPanel panel,String textArea,String fileName,Voice talk) {
		this.panel = panel;
		this.textArea = textArea;
		this.fileName = fileName;
		this.talk = talk;
		
		textArea1 = new JTextArea(textArea);
		textArea1.setBounds(10, 11, 300, 200);
		panel.add(textArea1);
		textArea1.enable(false);
		
		JLabel lblNewLabel = new JLabel("encoding:");
		lblNewLabel.setBounds(320, 50, 60, 15);
		panel.add(lblNewLabel);
		
		comboBox = new JComboBox();
		comboBox.setBounds(320, 66, 74, 20);
		panel.add(comboBox);
		comboBox.addItem("Atbash");
		comboBox.addItem("Rot-13");
		
		speechButton = new JButton("encode Speech");
		speechButton.setBounds(320, 130, 110, 22);
		panel.add(speechButton);
		
		lineEncodeSpeech = new JButton("line encode Speech");
		lineEncodeSpeech.setBounds(320, 170, 110, 22);
		panel.add(lineEncodeSpeech);
		
		backButton = new JButton("back");
		backButton.setBounds(335, 20, 89, 23);
		panel.add(backButton);
		
		speechButton.addActionListener(this);
		backButton.addActionListener(this);
		lineEncodeSpeech.addActionListener(this);
		
		
	}
	
	public void actionPerformed(ActionEvent e) {
		if(e.getSource()==speechButton) {
			String helpArray = "";
			//VoiceManager vs = VoiceManager.getInstance();
			//Voice talk = vs.getVoice("kevin16");
			int lineLength = 0;
			
			//spame to string se grammes
			String [] textFile = textArea.split("\n");
			for(String war : textFile) {
				lineLength++;
			}
			String reverseAlphabet = "zyxwvutsrqponmlkjihgfedcba";
			
			String reversed = "";
			for(int i = 5;i<lineLength;i++) {
				
				
				
				//spame to string se lexeis
				String [] word = textFile[i].split(" ");
				int wordLength = 0;
				for(String war : word) {
					wordLength++;
				}
				if(comboBox.getSelectedItem() == "Atbash") {
				
					for(int j = 0;j<wordLength;j++) {
						//System.out.println(word[j]);
						
						String es = "";
						
						String s = word[j];
						int k,h;
						char ch ;
						
						h = s.length();
						//spame to string se grammata kai kanoume thn katallhlh leitourgia kwdikopoihshs
						for(k=0;k<h;k++) {
							ch = s.charAt(k);
							if(Character.isUpperCase(ch)) {
								ch = reverseAlphabet.charAt(ch - 'A');
								
								es+=ch;
							}else {
								ch = reverseAlphabet.charAt(ch - 'a');
								
								es+=ch;
								
							}
							
						}
						//System.out.println(es);
						helpArray = helpArray + es +" ";
						
						
						
					}
					helpArray = helpArray +"\n";
					
					
					
				}
				else if(comboBox.getSelectedItem() == "Rot-13") {
					for(int j = 0;j<wordLength;j++) {
						//System.out.println(word[j]);
						
						String es = "";
						String s = word[j];
						int k,h;
						char ch ;
						
						h = s.length();
						for(k=0;k<h;k++) {
							ch = s.charAt(k);
							if(Character.isUpperCase(ch)) {
								ch+=13;
								if(ch>90) {
									ch-=26;
									
								}
								es+=ch;
							}else {
								ch+=13;
								if(ch>122) {
									ch-=26;
									
								}
								es+=ch;
								
							}
						}
						//System.out.println(es);
						helpArray = helpArray + es +" ";
						
					}
					helpArray = helpArray +"\n";
				}
				
				
			}
			System.out.println(helpArray);
			talk.allocate();
			talk.speak(helpArray);
			
		}
		//kanoume ta idia apla o xrhsths epilegei thn grammh
		else if(e.getSource()==lineEncodeSpeech) {
			String helpArray = "";
			//VoiceManager vs = VoiceManager.getInstance();
			//Voice talk = vs.getVoice("kevin16");
			int lineLength = 0;
			String [] textFile = textArea.split("\n");
			for(String war : textFile) {
				lineLength++;
			}
			String reverseAlphabet = "zyxwvutsrqponmlkjihgfedcba";
			String reversed = "";
			String lineNumber = JOptionPane.showInputDialog(null,"enter line number:");
			int IntLineNumber = parsInt(lineNumber);
			String [] word = textFile[IntLineNumber-1].split(" ");
			int wordLength = 0;
			for(String war : word) {
				wordLength++;
			}
			if(comboBox.getSelectedItem() == "Atbash") {
				
				for(int j = 0;j<wordLength;j++) {
					//System.out.println(word[j]);
						
					String es = "";
					String s = word[j];
					int k,h;
					char ch ;
						
					h = s.length();
					for(k=0;k<h;k++) {
						ch = s.charAt(k);
						if(Character.isUpperCase(ch)) {
							ch = reverseAlphabet.charAt(ch - 'A');
								
							es+=ch;
						}else {
							ch = reverseAlphabet.charAt(ch - 'a');
								
							es+=ch;
								
						}
							
					}
					//System.out.println(es);
					helpArray = helpArray + es +" ";
						
						
						
				}
				helpArray = helpArray +"\n";
						
			}
			else if(comboBox.getSelectedItem() == "Rot-13") {
				for(int j = 0;j<wordLength;j++) {
					//System.out.println(word[j]);
						
					String es = "";
					String s = word[j];
					int k,h;
					char ch ;
						
					h = s.length();
					for(k=0;k<h;k++) {
						ch = s.charAt(k);
						if(Character.isUpperCase(ch)) {
							ch+=13;
							if(ch>90) {
								ch-=26;
									
							}
							es+=ch;
						}else {
							ch+=13;
							if(ch>122) {
								ch-=26;
									
							}
							es+=ch;
								
						}
					}
					//System.out.println(es);
					helpArray = helpArray + es +" ";
						
				}
				helpArray = helpArray +"\n";
			}
			
			System.out.println(helpArray);
			talk.allocate();
			talk.speak(helpArray);
			
			
		}
		else if(e.getSource()==backButton) {
			CommandsFactory a = new CommandsFactory();
			panel.removeAll();
			panel.repaint();
			a.setPanel(panel);
			a.setTextArea(textArea);
			a.setFileName(fileName);
			a.setTalk(talk);
			a.createCommand("saveDoc");
			
		}
	}
	private int parsInt(String speechline) {
		int i = Integer.parseInt(speechline);
		return i;
	}
	
	/////////////////for the tests
	public String checkEncodeAtBash(String x) {

        String helpArea = "";
        String reverseAlphabet = "zyxwvutsrqponmlkjihgfedcba";
        String [] word = x.split(" ");
        int wordLength = 0;
        for(String war : word) {
            wordLength++;
        }
        for(int j = 0;j<wordLength;j++) {
            //System.out.println(word[j]);

            String es = "";
            String s = word[j];
            int k,h;
            char ch ;

            h = s.length();
            for(k=0;k<h;k++) {
                ch = s.charAt(k);
                if(Character.isUpperCase(ch)) {
                    ch = reverseAlphabet.charAt(ch - 'A');

                    es+=ch;
                }else {
                    ch = reverseAlphabet.charAt(ch - 'a');

                    es+=ch;

                }

            }

            helpArea = helpArea + es +" ";



        }
        System.out.println(helpArea);
        return helpArea;




    }
	
	public String checkEncodeRot13(String x) {
		String helpArray="";
        String [] word = x.split(" ");
        int wordLength = 0;
        for(String war : word) {
            wordLength++;
        }
        for(int j = 0;j<wordLength;j++) {
			
			
			String es = "";
			String s = word[j];
			int k,h;
			char ch ;
				
			h = s.length();
			for(k=0;k<h;k++) {
				ch = s.charAt(k);
				if(Character.isUpperCase(ch)) {
					ch+=13;
					if(ch>90) {
						ch-=26;
							
					}
					es+=ch;
				}else {
					ch+=13;
					if(ch>122) {
						ch-=26;
							
					}
					es+=ch;
						
				}
			}
			helpArray = helpArray + es +" ";
				
		}
        return helpArray;
        




    }
    public boolean ifTrueAtBash(String x , String y) {
        if(x.equals(y)) {

            return true;
        }
        else {
            return false;
        }
    }
    public boolean ifTrueRot13(String x , String y) {
        if(x.equals(y)) {

            return true;
        }
        else {
            return false;
        }
    }
    //////////////////////////////////////
    
    
}
