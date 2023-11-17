using UnityEngine;
using System.Collections;
using UnityEngine.SceneManagement;

public class menu : MonoBehaviour {

	public void jugarCuanCLick (){
		SceneManager.LoadScene("juego");
	}

	void QuitScene(){
		Application.Quit();
	}
	}
