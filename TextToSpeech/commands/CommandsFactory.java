package commands;

import java.awt.event.ActionListener;
import javax.swing.JPanel;

import com.sun.speech.freetts.Voice;


public class CommandsFactory {
	
    private NewDocument newDoc;
    private EditDocument editDoc;
    private SaveDocument saveDoc;
    private OpenDocument openDoc;
    private LineToSpeech lineDoc;
    private TuneEncoding encodingDoc;
    private TuneAudio audioDoc;
    private JPanel panel;
    private String textArea;
    private String fileName;
    private int flag;
    private Voice talk;
    
    public CommandsFactory() {
    	
    }
    
    public ActionListener createCommand(String s) {
        if(s.equals("newDoc")) {
            newDoc = new NewDocument(panel,talk);
            return newDoc;
        }
        else if(s.equals("editDoc")) {
        	
            editDoc = new EditDocument(panel,textArea,talk);
            return editDoc;
        }
        else if(s.equals("saveDoc")) {
        	
            saveDoc = new SaveDocument(panel,textArea,fileName,talk);
            return saveDoc;
        }
        else if(s.equals("openDoc")) {
        	openDoc = new OpenDocument(panel,talk);
        	return openDoc;
        }
        
        else if(s.equals("LineDoc")) {
        	lineDoc = new LineToSpeech(panel,fileName,flag,talk);
        	return lineDoc;
        }
        
        else if(s.equals("encodingDoc")) {
        	encodingDoc = new TuneEncoding(panel,textArea,fileName,talk);
        	return encodingDoc;
        }
        
        else if(s.equals("audioDoc")) {
        	audioDoc = new TuneAudio(talk);
        	audioDoc.setVisible(true);
        	return audioDoc;
        }
        
        return null;
    }
    public void setPanel(JPanel panel) {
    	this.panel = panel;
    }
   
    public void setTextArea(String textArea) {
    	this.textArea = textArea;
    }
    public void setFileName(String fileName) {
    	this.fileName = fileName;
    }
    public void setFlag(int flag) {
    	this.flag = flag;
    }
    
    public void setTalk(Voice talk) {
    	this.talk = talk;
    }
   
   
    
    
}