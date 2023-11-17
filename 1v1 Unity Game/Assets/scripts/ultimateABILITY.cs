using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class ultimateABILITY : MonoBehaviour {

	public float time;
	// Use this for initialization
	void Start () {
		time = 25;
		
	}
	
	// Update is called once per frame
	void Update () {
		time -= Time.deltaTime;
		if (time <= 0 && Input.GetKey("y")){
			SceneManager.LoadScene("habilidad ninja");


		}
	}
}
