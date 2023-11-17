using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;


public class tiempo_para_ulti : MonoBehaviour {
	public float time;
	public float tiempo;
	


	// Use this for initialization
	void Start () {
		time = 1;
		tiempo = 1.5f;
	}
	
	// Update is called once per frame
	void Update () {
		time -= Time.deltaTime;
		tiempo -= Time.deltaTime;

		if (time <= 0){
			this.GetComponent<Animator>().SetBool("dab", true);
		}
		if (tiempo <= 0 ){
			SceneManager.LoadScene("juego");
		}
		
	}
}
