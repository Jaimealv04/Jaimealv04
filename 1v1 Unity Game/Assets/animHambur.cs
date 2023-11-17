using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class animHambur : MonoBehaviour {
	public GameObject anim;
	// Use this for initialization
	void Start () {
		anim = GameObject.Find("personajeanimado");
		anim.GetComponent<Animator>().SetBool("running", false);
	}
	
	// Update is called once per frame
	void Update () {
		if(Input.GetKeyDown(KeyCode.RightArrow)){	
			anim.GetComponent<Animator>().SetBool("running", true);
		}
		if(Input.GetKeyDown(KeyCode.LeftArrow)){	
			anim.GetComponent<Animator>().SetBool("running", true);
		}
		if(Input.GetKeyUp(KeyCode.RightArrow)||Input.GetKeyUp(KeyCode.LeftArrow)){
			anim.GetComponent<Animator>().SetBool("running", false);
		}
	}
}
